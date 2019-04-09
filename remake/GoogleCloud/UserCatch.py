from GoogleCloud import sound_recorder, googleCloudSpeech

getUserOpinion = sound_recorder.getWaveFile()
getUserOpinion.run()
googleCloudSpeech.run_quickstart()

