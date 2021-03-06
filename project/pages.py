# -*- coding: utf-8 -*-
"""
The project pages map for project
"""
import io
import os

from optimus.builder.pages import PageViewBase
from optimus.conf import settings

from project import __version__ as sveetoy_version
from project.sitemap import PageSitemap, tree_from_directory_structure

from py_css_styleguide.model import Manifest

#sitemap_tree = tree_from_directory_structure(settings.TEMPLATES_DIR)
##sitemap_tree.show()


"""
Page objects
"""
class BasicPage(PageViewBase):
    """
    Basic page view
    """
    title = "Index"
    template_name = "index.html"
    destination = "index.html"
    foundation_version = 6

    def get_context(self):
        context = super(BasicPage, self).get_context()

        manifest = Manifest()
        manifest_filepath = os.path.join(settings.SOURCES_DIR, 'css', 'styleguide_manifest.css')
        with io.open(manifest_filepath, 'r') as fp:
            manifest.load(fp)

        context.update({
            'styleguide': manifest,
            'version': sveetoy_version,
            'foundation_version': self.foundation_version,
        })
        return context


class PageWithSitemap(BasicPage):
    """
    Page view aware of sitemap
    """
    sitemap = {}

    def get_context(self):
        context = super(PageWithSitemap, self).get_context()

        context.update({
            'site_sitemap': self.sitemap,
        })
        return context


# Enabled pages to build
#PAGES = PageSitemap(sitemap_tree, PageWithSitemap).ressources
PAGES = [
    BasicPage(),
    #BasicPage(foundation_version=5, template_name="index_f5.html", destination="f5/index.html"),
]
