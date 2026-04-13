# 发布清单

本文档用于王聚财面皮铺 Skill 发布到 GitHub 与 ClawHub 前的最终确认。

## 当前版本

- 版本号：`1.3.0`
- 公开下单入口：[美团点单](https://rms.meituan.com/diancan/14/2HpfZPxOFw0)
- 本地测试命令：`python3 -m unittest discover -s tests -v`

## 已完成事项

- 已移除公开仓库中的 Wi-Fi 密码
- 已移除二维码图片文件
- 已将二维码能力升级为公开下单入口
- 已补齐基础自动化测试
- 已补齐 MIT License 与 `.gitignore`

## 发布前必须确认

1. 将 `skill.json` 中的 `mcp_server.url` 替换为真实线上 MCP 地址
2. 确认 GitHub 仓库地址与 `skill.json` 中的 `repository` 一致
3. 确认公开下单链接仍然可用，且业务上允许直接公开给用户
4. 再次执行测试，确保返回的工具列表与文档一致
5. 确认门店电话、营业时间、地址、菜单价格为最新版本

## GitHub 发布建议

1. 不要直接从桌面根目录的大仓库发布
2. 建议将当前目录单独作为一个新仓库，或复制到独立目录后再初始化 Git
3. 提交前确认仓库内只有这些文件：
   - `README.md`
   - `SKILL.md`
   - `skill.json`
   - `mcp_server.py`
   - `tests/test_mcp_server.py`
   - `.gitignore`
   - `LICENSE`
   - `PUBLISHING.md`

## ClawHub 发布建议

1. 先完成线上 MCP 部署
2. 在 ClawHub 填写真实 MCP 地址
3. 确认工具名称与用途：
   - `get_restaurant_info`
   - `get_menu`
   - `get_delivery_info`
   - `get_reservation_info`
   - `get_wifi_info`
   - `get_order_entry`
4. 描述中强调：
   - AI 可直接提供公开下单链接
   - 用户到店后也可以扫桌面二维码进入同一入口

## 发布后建议

- 每次菜单或营业时间变更时同步更新 `SKILL.md`、`skill.json` 和 `mcp_server.py`
- 如果更换下单入口，优先更新 `get_order_entry` 返回的链接
- 如后续接入真实订单 API，可将当前“入口型 Skill”升级为“可下单 Skill”
