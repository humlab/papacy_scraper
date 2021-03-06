import types
import unittest

from .utils import create_test_files_reader

class test_FileTextReader(unittest.TestCase):

    def test_archive_filenames_when_filter_txt_returns_txt_files(self):
        reader = create_test_files_reader(pattern='*.txt')
        self.assertEqual(5, len(reader.archive_filenames))

    def test_archive_filenames_when_filter_md_returns_md_files(self):
        reader = create_test_files_reader(pattern='*.md')
        self.assertEqual(1, len(reader.archive_filenames))

    def test_archive_filenames_when_filter_function_txt_returns_txt_files(self):
        itemfilter = lambda _, x: x.endswith('txt')
        reader = create_test_files_reader(itemfilter=itemfilter)
        self.assertEqual(5, len(reader.archive_filenames))

    def test_get_file_when_default_returns_unmodified_content(self):
        document_name = 'dikt_2019_01_test.txt'
        reader = create_test_files_reader(compress_whitespaces=False, dehyphen=True)
        result = next(reader.get_file(document_name))
        expected = "Tre svarta ekar ur snön.\r\n" + \
                   "Så grova, men fingerfärdiga.\r\n" + \
                   "Ur deras väldiga flaskor\r\n" + \
                   "ska grönskan skumma i vår."
        self.assertEqual(document_name, result[0])
        self.assertEqual(expected, result[1])

    def test_can_get_file_when_compress_whitespace_is_true_strips_whitespaces(self):
        document_name = 'dikt_2019_01_test.txt'
        reader = create_test_files_reader(compress_whitespaces=True, dehyphen=True)
        result = next(reader.get_file(document_name))
        expected = "Tre svarta ekar ur snön. " + \
                   "Så grova, men fingerfärdiga. " + \
                   "Ur deras väldiga flaskor " + \
                   "ska grönskan skumma i vår."
        self.assertEqual(document_name, result[0])
        self.assertEqual(expected, result[1])

    def test_get_file_when_dehyphen_is_trye_removes_hyphens(self):
        document_name = 'dikt_2019_03_test.txt'
        reader = create_test_files_reader(compress_whitespaces=True, dehyphen=True)
        result = next(reader.get_file(document_name))
        expected = "Nordlig storm. Det är den i den tid när rönnbärsklasar mognar. Vaken i mörkret hör man " + \
                   "stjärnbilderna stampa i sina spiltor " + \
                   "högt över trädet"
        self.assertEqual(document_name, result[0])
        self.assertEqual(expected, result[1])

    def test_get_file_when_file_exists_and_extractor_specified_returns_content_and_metadat(self):
        document_name = 'dikt_2019_03_test.txt'
        meta_extract = dict(year=r".{5}(\d{4})_.*", serial_no=r".{9}_(\d+).*")
        reader = create_test_files_reader(meta_extract=meta_extract, compress_whitespaces=True, dehyphen=True)
        result = next(reader.get_file(document_name))
        expected = "Nordlig storm. Det är den i den tid när rönnbärsklasar mognar. Vaken i mörkret hör man " + \
                   "stjärnbilderna stampa i sina spiltor " + \
                   "högt över trädet"
        self.assertEqual(document_name, result[0].filename)
        self.assertEqual(2019, result[0].year)
        self.assertEqual(3, result[0].serial_no)
        self.assertEqual(expected, result[1])

    def test_get_index_when_extractor_passed_returns_metadata(self):
        meta_extract = dict(year=r".{5}(\d{4})_.*", serial_no=r".{9}_(\d+).*")
        reader = create_test_files_reader(meta_extract=meta_extract, compress_whitespaces=True, dehyphen=True)
        result = reader.metadata
        expected = [
            types.SimpleNamespace(filename='dikt_2019_01_test.txt', serial_no=1, year=2019),
            types.SimpleNamespace(filename='dikt_2019_02_test.txt', serial_no=2, year=2019),
            types.SimpleNamespace(filename='dikt_2019_03_test.txt', serial_no=3, year=2019),
            types.SimpleNamespace(filename='dikt_2020_01_test.txt', serial_no=1, year=2020),
            types.SimpleNamespace(filename='dikt_2020_02_test.txt', serial_no=2, year=2020)]

        self.assertEqual(len(expected), len(result))
        for i in range(0,len(expected)):
            self.assertEqual(expected[i], result[i])

