import json

SITE_DATA = {
    "name": "爱游戏门户",
    "url": "https://m-portal-i-game.com.cn",
    "keywords": ["爱游戏", "手游", "游戏门户", "游戏社区", "游戏资讯"],
    "tags": ["游戏", "门户", "手机游戏", "娱乐"],
    "description": "爱游戏平台是一个集合手游资讯、游戏社区和游戏推荐的门户网站，致力于为玩家提供丰富的游戏内容和互动体验。"
}

SITES = [
    SITE_DATA,
    {
        "name": "爱游戏助手",
        "url": "https://m-portal-i-game.com.cn/assistant",
        "keywords": ["爱游戏", "游戏助手", "工具", "攻略"],
        "tags": ["工具", "攻略", "手机游戏"],
        "description": "提供游戏攻略、工具和实用功能，帮助玩家提升游戏体验。"
    },
    {
        "name": "爱游戏社区",
        "url": "https://m-portal-i-game.com.cn/community",
        "keywords": ["爱游戏", "社区", "玩家交流", "论坛"],
        "tags": ["社区", "交流", "论坛"],
        "description": "玩家交流社区，分享游戏心得、组队信息和最新动态。"
    }
]


def format_site_summary(site: dict) -> str:
    lines = []
    lines.append(f"站点名称: {site['name']}")
    lines.append(f"URL: {site['url']}")
    lines.append(f"关键词: {', '.join(site['keywords'])}")
    lines.append(f"标签: {', '.join(site['tags'])}")
    lines.append(f"描述: {site['description']}")
    return "\n".join(lines)


def generate_full_summary(sites: list) -> str:
    sections = []
    for idx, site in enumerate(sites, 1):
        header = f"--- 站点 {idx} ---"
        body = format_site_summary(site)
        sections.append(f"{header}\n{body}")
    return "\n\n".join(sections)


def save_summary_to_file(content: str, filepath: str = "site_summary_output.txt") -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"摘要已保存至 {filepath}")


def print_summary(content: str) -> None:
    print("========== 站点结构化摘要 ==========")
    print(content)
    print("====================================")


def main():
    summary = generate_full_summary(SITES)
    print_summary(summary)
    save_summary_to_file(summary)


if __name__ == "__main__":
    main()