import sda
va = sda.VideoAnimator(model_path="C:/Users/Robijntje/Documents/EHB/FP3/speech-driven-animation-master/sda/data/grid.dat")# Instantiate the animator

vid, aud = va("C:/Users/Robijntje/Documents/EHB/FP3/speech-driven-animation-master/example/robin.jpg", "C:/Users/Robijntje/Documents/EHB/FP3/speech-driven-animation-master/example/audio9.wav")
va.save_video(vid, aud, "./generated.mp4")  