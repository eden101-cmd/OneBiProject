def separate_transcripts(transcript_text):
    """
    Processes a transcript text to separate transcripts.
    Args:
        transcript_text (str): The input text containing multiple transcripts.
    Returns:
        list of str: A list of separated transcripts extracted from the input text.
    """
    lines = transcript_text.strip().split('\n')

    transcripts = []
    current_transcript = ""

    for line in lines:
        if line.startswith("Transcript"):
            if current_transcript:
                transcripts.append(current_transcript.strip())
            current_transcript = line + "\n"
        else:
            current_transcript += line + "\n"

    if current_transcript:
        transcripts.append(current_transcript.strip())

    return transcripts

