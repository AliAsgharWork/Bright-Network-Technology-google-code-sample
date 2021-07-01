"""A video player class."""
import random
from .video_library import VideoLibrary
# key to identify function status
# LOOKS CLEAR
# DONE
# LATER


class VideoPlayer:
    """A class used to represent a Video Player."""
    last_played_video = []
    pause_status = False

    def __init__(self):
        self._video_library = VideoLibrary()

    def is_last_played_video_empty(self):
        return bool(len(self.last_played_video) == 0)

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):  # DONE
        """Returns all videos."""
        all_videos_list = self._video_library.get_all_videos()
        # Sort it according to title
        all_videos_list_sorted = sorted(all_videos_list, key=lambda l: l.title)

        print("Here's a list of all available videos:")
        for video in all_videos_list_sorted:
            vidtag = " ".join(video.tags)
            print(f" {video.title} ({video.video_id}) [{vidtag}]")

    def play_video(self, video_id):  # LATER
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        """use cases
        play video shows play + title
        new vid shows stop old vid and playing new vid
        same vid stop +title and start + title

        invalid input shows does not exist"""

        # get the video
        video = self._video_library.get_video(video_id)

        if(video == None):  # If the video ID is invalid
            # if(len(self.last_played_video) != 0):#invalid input and video was playing
            #     print(f"Stopping video: {self.last_played_video[-1].title}")
            return print("Cannot play video: Video does not exist")

        # unpause the video
        self.pause_status = False

        if(self.is_last_played_video_empty()):
            # play vid
            print(f"Playing video: {video.title}")
        else:
            print(f"Stopping video: {self.last_played_video[-1].title}")
            print(f"Playing video: {video.title}")

        self.last_played_video.append(video)

    def stop_video(self):  # LOOKS CLEAR
        """Stops the current video."""
        if(self.is_last_played_video_empty()):
            return print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self.last_played_video[-1].title}")

        self.last_played_video.clear()
        self.pause_status == False

    def play_random_video(self):  # LATER
        """Plays a random video from the video library."""
        all_videos_list = self._video_library.get_all_videos()
        number_of_videos = len(self._video_library.get_all_videos())
        # Random number will never be greater then the avaliable videos
        random_number = random.randrange(number_of_videos)
        self.play_video(all_videos_list[random_number]._video_id)

    def pause_video(self):
        """Pauses the current video."""
        """edge cases
        pause video
        video is paused
        stop video/not video playing and enter pause"""
        if(self.is_last_played_video_empty()):
            return print("Cannot pause video: No video is currently playing")
        if(self.pause_status == False):
            print(f"Pausing video: {self.last_played_video[-1].title}")
            self.pause_status = True
        elif(self.pause_status == True):
            print(f"Video already paused: {self.last_played_video[-1].title}")

    def continue_video(self):
        """Resumes playing the current video."""
        if(self.is_last_played_video_empty()):
            return print("Cannot continue video: Video is not paused")
        if(self.pause_status == True):
            print(f"Continuing video: {self.last_played_video[-1].title}")
            self.pause_status = False
        elif(self.pause_status == False):
            print("Cannot continue video: Video is not paused")

        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        if(self.is_last_played_video_empty()):
            return print("No video is currently playing")

        current_playing_video = self.last_played_video[-1]._video_id
        video = self._video_library.get_video(current_playing_video)
        vidtag = " ".join(video.tags)
        show = (f"{video.title} ({video.video_id}) [{vidtag}]")

        if(self.pause_status == True):
            print("Currently playing:", show, " - PAUSED")
        elif(self.pause_status == False):
            print("Currently playing:", show)
        # print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
