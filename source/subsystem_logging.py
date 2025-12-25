def _log_debug_command(msg, *args, **kwargs):
    """A wrapper for command subsystem debug logs."""
    _log.debug(msg, *args, extra={"subsystem": SNAPM_SUBSYSTEM_COMMAND}, **kwargs)
