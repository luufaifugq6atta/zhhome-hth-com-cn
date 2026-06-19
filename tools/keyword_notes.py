from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class KeywordNote:
    """
    表示一条关键词笔记的数据类。
    """
    keyword: str
    url: str
    note: str = ""
    created_at: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display(self) -> str:
        """返回单条笔记的格式化字符串。"""
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"关键词：{self.keyword}\n"
            f"关联网址：{self.url}\n"
            f"笔记：{self.note}\n"
            f"创建时间：{self.created_at}\n"
            f"标签：{tag_str}\n"
        )


@dataclass
class KeywordNoteCollection:
    """
    关键词笔记集合，支持添加、查找、格式化输出。
    """
    notes: List[KeywordNote] = field(default_factory=list)

    def add(self, note: KeywordNote) -> None:
        """添加一条笔记。"""
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> List[KeywordNote]:
        """根据关键词查找笔记（模糊匹配）。"""
        return [
            note for note in self.notes
            if keyword.lower() in note.keyword.lower()
        ]

    def find_by_tag(self, tag: str) -> List[KeywordNote]:
        """根据标签查找笔记。"""
        return [
            note for note in self.notes
            if any(tag.lower() in t.lower() for t in note.tags)
        ]

    def format_all(self) -> str:
        """格式化输出所有笔记。"""
        if not self.notes:
            return "暂无笔记。"
        parts = ["关键词笔记列表：", "=" * 40]
        for i, note in enumerate(self.notes, 1):
            parts.append(f"笔记 #{i}")
            parts.append(note.display())
            parts.append("-" * 40)
        return "\n".join(parts)

    def summary(self) -> str:
        """返回简要统计信息。"""
        return f"共收录 {len(self.notes)} 条关键词笔记。"


def demo() -> None:
    """演示如何使用 KeywordNoteCollection。"""
    collection = KeywordNoteCollection()

    # 添加示例笔记：使用给定的 URL 和关键词
    note1 = KeywordNote(
        keyword="华体会",
        url="https://zhhome-hth.com.cn",
        note="这是华体会相关的主页链接。",
        tags=["体育", "娱乐"],
    )
    note2 = KeywordNote(
        keyword="华体会活动",
        url="https://zhhome-hth.com.cn/events",
        note="近期活动页面。",
        tags=["体育", "活动"],
    )
    note3 = KeywordNote(
        keyword="华体会登录",
        url="https://zhhome-hth.com.cn/login",
        note="用户登录入口。",
        tags=["登录", "账户"],
    )

    collection.add(note1)
    collection.add(note2)
    collection.add(note3)

    # 输出全部笔记
    print(collection.format_all())
    print(collection.summary())

    # 按关键词查找
    print("\n查找包含“华体会”的笔记：")
    for note in collection.find_by_keyword("华体会"):
        print(note.display())

    # 按标签查找
    print("查找标签为“体育”的笔记：")
    for note in collection.find_by_tag("体育"):
        print(note.display())


if __name__ == "__main__":
    demo()