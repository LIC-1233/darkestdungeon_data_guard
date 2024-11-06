import re
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element


class xml_data:
    mod_title: str
    mod_versions: list[int]
    mod_tags: list[str]
    mod_description: str
    mod_PublishedFileId: str

    def __init__(
        self,
        mod_title: str,
        mod_versions: list[int],
        mod_tags: list[str],
        mod_description: str,
        mod_PublishedFileId: str,
    ):
        self.mod_title = mod_title
        self.mod_versions = mod_versions
        self.mod_tags = mod_tags
        self.mod_description = mod_description
        self.mod_PublishedFileId = mod_PublishedFileId

    @classmethod
    def etree_text_iter(cls, tree: Element, name: str):
        for elem in tree.iter(name):
            if isinstance(elem.text, str):
                return elem.text
        return ""

    @classmethod
    def mod_xml_parser(cls, xml_file: str | Path):
        mod_title: str = ""
        mod_versions: list[int] = [0, 0, 0]
        mod_tags: list[str] = []
        mod_description: str = ""
        mod_PublishedFileId: str = ""
        tree = ET.parse(xml_file)
        if not tree:
            return cls(
                mod_title, mod_versions, mod_tags, mod_description, mod_PublishedFileId
            )
        root = tree.getroot()
        mod_title = cls.etree_text_iter(root, "Title") or mod_title
        mod_title = re.sub(r'[\/:*?"<>|]', "_", mod_title).strip()
        mod_versions[0] = int(
            cls.etree_text_iter(root, "VersionMajor") or mod_versions[0]
        )
        mod_versions[1] = int(
            cls.etree_text_iter(root, "VersionMinor") or mod_versions[1]
        )
        mod_versions[2] = int(
            cls.etree_text_iter(root, "TargetBuild") or mod_versions[2]
        )
        mod_description = (
            cls.etree_text_iter(root, "ItemDescription") or mod_description
        )
        mod_PublishedFileId = (
            cls.etree_text_iter(root, "PublishedFileId") or mod_PublishedFileId
        )
        for Tags in root.iter("Tags"):
            if not isinstance(Tags.text, str) or not Tags.text.strip():
                continue
            mod_tags.append(Tags.text)
        return cls(
            mod_title, mod_versions, mod_tags, mod_description, mod_PublishedFileId
        )
