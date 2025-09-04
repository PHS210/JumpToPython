import os

def generate_tree_md(root_dir, indent=""):
    items = sorted(os.listdir(root_dir))
    tree_lines = []
    for i, item in enumerate(items):
        path = os.path.join(root_dir, item)
        connector = "┗" if i == len(items) - 1 else "┣"

        if os.path.isdir(path):
            tree_lines.append(f"{indent}{connector} {item}/")
            tree_lines.extend(generate_tree_md(path, indent + "┃ "))
        else:
            # 파일이면 체크박스 스타일로 출력
            tree_lines.append(f"{indent}{connector} [ ] {item}")

    return tree_lines

if __name__ == "__main__":
    root = "./초위파300제"  # 현재 폴더 기준
    tree_md = generate_tree_md(root)
    print("## 📂 프로젝트 구조 & 진행 현황\n")
    print("```\n" + "\n".join(tree_md) + "\n```")
