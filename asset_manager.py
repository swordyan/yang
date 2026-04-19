#!/usr/bin/env python3
"""简单的资产管理脚本：支持录入和查询。"""

from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path("assets.json")


def load_assets() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def save_assets(assets: list[dict]) -> None:
    DATA_FILE.write_text(
        json.dumps(assets, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def add_asset(assets: list[dict]) -> None:
    name = input("资产名称: ").strip()
    category = input("资产类别: ").strip()

    while True:
        amount_raw = input("资产金额: ").strip()
        try:
            amount = float(amount_raw)
            break
        except ValueError:
            print("金额格式不正确，请输入数字。")

    note = input("备注(可选): ").strip()

    asset = {
        "name": name,
        "category": category,
        "amount": amount,
        "note": note,
    }
    assets.append(asset)
    save_assets(assets)
    print("\n✅ 资产录入成功。")


def query_assets(assets: list[dict]) -> None:
    keyword = input("输入关键字(名称/类别，留空查看全部): ").strip().lower()
    if keyword:
        results = [
            a
            for a in assets
            if keyword in a.get("name", "").lower()
            or keyword in a.get("category", "").lower()
        ]
    else:
        results = assets

    if not results:
        print("\n未找到匹配资产。")
        return

    print("\n查询结果:")
    print("-" * 60)
    total = 0.0
    for idx, asset in enumerate(results, start=1):
        total += float(asset.get("amount", 0))
        print(
            f"{idx}. 名称: {asset.get('name', '')} | "
            f"类别: {asset.get('category', '')} | "
            f"金额: {asset.get('amount', 0):.2f} | "
            f"备注: {asset.get('note', '')}"
        )
    print("-" * 60)
    print(f"合计金额: {total:.2f}")


def main() -> None:
    assets = load_assets()

    while True:
        print("\n=== 资产管理 ===")
        print("1. 录入资产")
        print("2. 查询资产")
        print("3. 退出")
        choice = input("请选择操作: ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            query_assets(assets)
        elif choice == "3":
            print("已退出。")
            break
        else:
            print("无效选择，请重试。")


if __name__ == "__main__":
    main()
