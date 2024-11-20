import isodate

def parse_duration(iso_duration):
    """
    Converts ISO 8601 duration into a readable UTC format (HH:MM:SS).

    Args:
        iso_duration: ISO 8601 duration string (e.g., "PT1H30M20S").

    Returns:
        Duration in HH:MM:SS format, or "00:00:00" if the input is invalid.
    """
    try:
        if not iso_duration:
            return "00:00:00"
        duration = isodate.parse_duration(iso_duration)
        hours, remainder = divmod(duration.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    except Exception as e:
        print(f"Error parsing duration: {iso_duration} - {e}")
        return "00:00:00"
