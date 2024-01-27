from Transcripts import extract_transcriptions,make_Transcript
def separate_transcripts(transcript_text):
    # Split the transcript text into individual lines
    lines = transcript_text.strip().split('\n')

    # Initialize variables
    transcripts = []
    current_transcript = ""

    # Iterate through each line
    for line in lines:
        # Check if the line starts with "Transcript"
        if line.startswith("Transcript"):
            # If a transcript is already in progress, add it to the list
            if current_transcript:
                transcripts.append(current_transcript.strip())
            # Start a new transcript
            current_transcript = line + "\n"
        else:
            # Add the line to the current transcript
            current_transcript += line + "\n"

    # Add the last transcript to the list
    if current_transcript:
        transcripts.append(current_transcript.strip())

    return transcripts

file_path = r'C:\Users\cohen\Downloads\תמלולי שיחות.docx'
transcriptions = extract_transcriptions(file_path)
Transcriptions = make_Transcript(transcriptions)
print(separate_transcripts(Transcriptions))