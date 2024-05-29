# bittorrent_client.py
from abc import ABC, abstractmethod

class BittorrentClient(ABC):
    @abstractmethod
    def add_torrent(self, torrent_file, category, tags, is_paused):
        """Add a new torrent."""
        pass

    @abstractmethod
    def get_torrent_info(self, status_filter, category, tags, sort, reverse):
        """Retrieve information about torrents."""
        pass

    @abstractmethod
    def get_files(self, torrent_hash):
        """Get files for a specific torrent."""
        pass

    @abstractmethod
    def rename_file(self, torrent_hash, old_path, new_path):
        """Rename a file within a torrent."""
        pass

    @abstractmethod
    def rename_folder(self, torrent_hash, old_path, new_path):
        """Rename a folder within a torrent."""
        pass

    @abstractmethod
    def rename_torrent(self, torrent_hash, new_torrent_name):
        """Rename a torrent."""
        pass

    @abstractmethod
    def resume_torrent(self, torrent_hashes):
        """Resume paused torrents."""
        pass

    @abstractmethod
    def delete_torrent(self, delete_files, torrent_hashes):
        """Delete torrents."""
        pass

    @abstractmethod
    def recheck_torrent(self, torrent_hashes):
        """Recheck torrents."""
        pass