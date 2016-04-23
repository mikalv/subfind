from pprint import pprint

import shutil
from os.path import getsize, exists
from subfind_provider_subscene import SubsceneProvider
from tempfile import mkdtemp

__author__ = 'hiepsimu'
import logging
import unittest

logging.basicConfig(level=logging.DEBUG)


class SubsceneTestCase(unittest.TestCase):
    def setUp(self):
        self.provider = SubsceneProvider()

    # def test_search_movie(self):
    #     movies = self.provider.search_movie({
    #         'title_query': 'the hobbit'
    #     })
    #
    #     # pprint(movies)
    #
    #     self.assertTrue(movies is not None)
    #     self.assertTrue(isinstance(movies, list))
    #     self.assertTrue(len(movies) > 0)
    #
    # def test_get_movie_subs(self):
    #     movie = {'title': 'The Hobbit: An Unexpected Journey',
    #              'url': 'http://subscene.com/subtitles/the-hobbit-an-unexpected-journey',
    #              'year': 2012}
    #     params = {}
    #     subtitles = self.provider.get_movie_subs(movie, params, 'en')
    #
    #     # pprint(subtitles)
    #
    #     self.assertTrue(subtitles is not None)
    #     self.assertTrue(isinstance(subtitles, list))
    #     self.assertTrue(len(subtitles) > 0)
    #
    # def test_get_sub(self):
    #     testcases = [
    #         # Format: release, expected_ext, expected_size
    #         # Zip sub
    #         (
    #             {'name': 'sub',
    #              'url': 'http://subscene.com/subtitles/the-divergent-series-insurgent/vietnamese/1151452',
    #              'lang': 'vi'},
    #             'srt',
    #             149392
    #         ),
    #         # Rar sub
    #         (
    #             {'name': 'sub',
    #              'url': 'http://subscene.com/subtitles/game-of-thrones-first-season/vietnamese/433869',
    #              'lang': 'vi'},
    #             'ass',
    #             86907
    #         )
    #     ]
    #     for release, expected_ext, expected_size in testcases:
    #         sub_dir = mkdtemp()
    #         try:
    #             subtitle = self.provider.get_sub(release)
    #
    #             # print(subtitle.path)
    #             self.assertTrue(subtitle.path.endswith('/%s.%s.%s' % (release['name'], release['lang'], expected_ext)))
    #             self.assertTrue(exists(subtitle.path))
    #             self.assertEqual(expected_size, getsize(subtitle.path))
    #             # print(get_file_content(subtitle.path))
    #         finally:
    #             shutil.rmtree(sub_dir)

    def test_search_release(self):
        testcases = [
            # failed cases
            # ('Boardwalk.Empire.S01E01.720p.HDTV.x264-IMMERSE', ['en', 'vi']),
            # ('Game of Thrones S01E03 Lord Snow 1080p 5.1', ['vi']),

            # pass cases
            # ('black.mass.2015.1080p.bluray.6ch.hevc.x265.rmteam', ['vi']),
            # ('Men.In.Black.II.2002.1080p.BluRay.x264.YIFY', ['vi']),
            # ('Tammy.2014.1080p.BluRay.x264.YIFY', ['vi']),
            # ('Brick.Mansions.2014.1080p.BluRay.x264.YIFY', ['vi']),
            # ('Burnt.2015.1080p.BluRay.6CH.1.8GB.MkvCage', ['vi']),
            # ('Avengers.Age.of.Ultron.2015.1080p.BluRay.x264.YIFY', ['vi']),
            # ('The.Benefactor.2015.1080p.WEB-DL.DD5.1.H264-FGT', ['en']),
            ('13.2010.720p.BluRay.x264.YIFY', ['vi']),
        ]

        for release_name, langs in testcases:
            releases = self.provider.get_releases(release_name, langs)

            pprint(releases)

            self.assertTrue(releases is not None)
            self.assertTrue(isinstance(releases, dict))
            self.assertTrue(len(releases.keys()) > 0)

            for lang in releases:
                self.assertTrue(lang in langs)
                self.assertTrue(len(releases[lang]) > 0)


if __name__ == '__main__':
    unittest.main()
