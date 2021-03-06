# -*- coding: utf-8 -*-
import pytest
import datetime as dt

from config import DataFolder
from config import PathHelper, DateHelper


@pytest.mark.skip()
def test_md(folder):
    assert False


class Test_Folder():
    def test_repr(self):
        assert repr(DataFolder(2015, 5))

    def test_get_folder_methods_return_existing_folders(self):
        assert DataFolder(2015, 5).get_processed_folder().exists()
        assert DataFolder(2015, 5).get_interim_folder().exists()

    @pytest.mark.skip
    def test_raw_folder_may_not_be_present(self):
        assert DataFolder(2015, 5).get_raw_folder().exists()

    def test_get_interim_csv_method_returns_existing_file(self):
        assert DataFolder(2015, 5).get_interim_csv().exists()

    def test_out_of_range_year_does_raises_error(self):
        with pytest.raises(ValueError):
            DataFolder(2030, 1)

# skipping


@pytest.mark.skip(reason="not testing maintenance scripts yet")
def test_copy_latest():
    assert False


class Test_PathHelper:

    def test_locate_csv_on_year_month_path_esists(self):
        assert PathHelper.locate_csv(2017, 5).exists() is True

    def test_get_processed_folder_returns_existing_folder(self):
        assert PathHelper.get_processed_folder(2017, 5).exists() is True

    def test_get_processed_folder_will_not_work_without_arguments(self):
        with pytest.raises(TypeError):
            PathHelper.get_processed_folder()


class Test_DateHelper:

    def test_validate_passes(self):
        DateHelper.validate(2015, 6)

    def test_validate_failes(self):
        with pytest.raises(ValueError):
            DateHelper.validate(2030, 1)

    def test_get_latest_date(self):
        year, month = DateHelper.get_latest_date()
        assert year >= 2017
        assert month >= 1
        assert month <= 12

    def test_get_supported_dates_starts_in_2009_4(self):
        assert DateHelper.get_supported_dates()[0] == (2009, 4)

    def test_get_supported_dates_ends_with_latest_date(self):
        prev_month_date = dt.datetime.today().replace(day=1) - dt.timedelta(days=1)
        assert DateHelper.get_supported_dates()[-1] == (prev_month_date.year,
                                                        prev_month_date.month)

    def test_get_supported_dates_excludes_2013_11(self):
        assert (2013, 11) not in DateHelper.get_supported_dates()


@pytest.mark.skip(reason="not testing maintenance scripts yet")
def test_init_dirs():
    assert False


if __name__ == "__main__":
    pytest.main([__file__])
