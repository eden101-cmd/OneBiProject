def separate_transcripts(transcript_text):
    """this function takes a transcript_text input and processes
    it to separate individual transcripts."""
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
