import numpy as np

class ImplicitRecommender:
    def __init__(self):
        self.user_profile = np.zeros(4)

    def watch(self, video_vector, seconds_watched):
        weight = min(seconds_watched / 60, 1)
        self.user_profile += np.array(video_vector) * weight

    def score(self, video_vector):
        return float(np.dot(self.user_profile, video_vector))
