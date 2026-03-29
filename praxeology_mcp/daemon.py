"""General-purpose daemon process manager for Praxeology ecosystem."""

import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path


class DaemonManager:
    """Manages background daemon processes via PID files."""

    def __init__(self, pid_dir: str = None):
        self.pid_dir = Path(pid_dir or Path.home() / ".claude" / "praxeology" / "pids")
        self.pid_dir.mkdir(parents=True, exist_ok=True)

    def _pid_file(self, name: str) -> Path:
        return self.pid_dir / f"{name}.pid"

    def start(self, target_module: str, target_func: str, name: str,
              args: dict = None, python: str = None) -> dict:
        """Start a daemon process.

        Args:
            target_module: Python module path (e.g., 'praxeology_mcp.heartbeat')
            target_func: Function to call (e.g., 'run_daemon')
            name: Daemon name for PID file
            args: Dict of kwargs to pass as JSON
            python: Python executable path (defaults to current)
        """
        pid_file = self._pid_file(name)

        # Check if already running
        if pid_file.exists():
            try:
                pid = int(pid_file.read_text().strip())
            except (ValueError, PermissionError, OSError):
                pid_file.unlink(missing_ok=True)
                pid = None
            if pid is not None:
                try:
                    os.kill(pid, 0)
                    return {"status": "already_running", "pid": pid, "name": name}
                except ProcessLookupError:
                    pid_file.unlink(missing_ok=True)

        python = python or sys.executable

        env = os.environ.copy()
        if args:
            env["_DAEMON_ARGS"] = json.dumps(args)

        code = (
            f"import os, json; "
            f"kwargs = json.loads(os.environ.get('_DAEMON_ARGS', '{{}}')); "
            f"from {target_module} import {target_func}; "
            f"{target_func}(**kwargs)"
        )

        proc = subprocess.Popen(
            [python, "-c", code],
            start_new_session=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            env=env,
        )
        pid_file.write_text(str(proc.pid))
        return {"status": "started", "pid": proc.pid, "name": name}

    def stop(self, name: str) -> dict:
        """Stop a daemon by name."""
        pid_file = self._pid_file(name)
        if not pid_file.exists():
            return {"status": "not_running", "name": name}

        try:
            pid = int(pid_file.read_text().strip())
        except (ValueError, PermissionError, OSError):
            pid_file.unlink(missing_ok=True)
            return {"name": name, "running": False, "pid": None, "error": "corrupt_pid_file"}

        try:
            os.kill(pid, signal.SIGTERM)
            # Wait up to 1 second for clean shutdown
            for _ in range(10):
                try:
                    os.kill(pid, 0)
                    time.sleep(0.1)
                except ProcessLookupError:
                    break
            else:
                # Still running after 1s — force kill
                try:
                    os.kill(pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            result = {"status": "stopped", "pid": pid, "name": name}
        except ProcessLookupError:
            result = {"status": "was_not_running", "pid": pid, "name": name}

        pid_file.unlink(missing_ok=True)
        return result

    def status(self, name: str) -> dict:
        """Check daemon status."""
        pid_file = self._pid_file(name)
        if not pid_file.exists():
            return {"name": name, "running": False, "pid": None}

        try:
            pid = int(pid_file.read_text().strip())
        except (ValueError, PermissionError, OSError):
            pid_file.unlink(missing_ok=True)
            return {"name": name, "running": False, "pid": None, "error": "corrupt_pid_file"}

        try:
            os.kill(pid, 0)
            return {"name": name, "running": True, "pid": pid}
        except ProcessLookupError:
            return {"name": name, "running": False, "pid": pid, "stale": True}

    def list_all(self) -> list:
        """List all known daemons."""
        results = []
        for pid_file in self.pid_dir.glob("*.pid"):
            name = pid_file.stem
            results.append(self.status(name))
        return results

    def stop_all(self) -> list:
        """Stop all daemons."""
        results = []
        for pid_file in self.pid_dir.glob("*.pid"):
            name = pid_file.stem
            results.append(self.stop(name))
        return results
