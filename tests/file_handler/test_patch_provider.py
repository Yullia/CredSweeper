from unittest.mock import Mock, patch
        patch_provider = PatchProvider([str(file_path)], "added")
    def test_load_patch_data_utf16_n(self) -> None:
        patch_provider = PatchProvider([str(file_path)], "added")
        with patch('logging.Logger.info') as mocked_logger:
            raw_patches = patch_provider.load_patch_data()
            warning_message = f"UnicodeError: Can't read content from \"{file_path}\" as utf8."
            mocked_logger.assert_called_with(warning_message)
    def test_load_patch_data_western_n(self) -> None:
        patch_provider = PatchProvider([str(file_path)], "added")
        with patch('logging.Logger.info') as mocked_logger:
            raw_patches = patch_provider.load_patch_data()
            warning_message = f"UnicodeError: Can't read content from \"{file_path}\" as utf16."
            mocked_logger.assert_called_with(warning_message)
        patch_provider = PatchProvider([str(file_path)], "added")
        with patch('logging.Logger.info') as mocked_logger:
            raw_patches = patch_provider.load_patch_data()
            warning_message = f"UnicodeError: Can't read content from \"{file_path}\" as utf16."
            mocked_logger.assert_called_with(warning_message)