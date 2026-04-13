import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import mcp_server


class MCPServerTests(unittest.TestCase):
    def test_initialize_uses_jsonrpc_wrapper(self) -> None:
        response = mcp_server.handle_mcp_request(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {},
            }
        )
        self.assertEqual(response["jsonrpc"], "2.0")
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["result"]["serverInfo"]["version"], mcp_server.SERVER_VERSION)

    def test_unknown_tool_returns_standard_error(self) -> None:
        response = mcp_server.handle_mcp_request(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {"name": "not_found"},
            }
        )
        self.assertEqual(response["error"]["code"], -32601)
        self.assertIn("Unknown tool", response["error"]["message"])

    def test_wifi_payload_does_not_expose_password(self) -> None:
        payload = json.loads(mcp_server.get_wifi_info()["content"][0]["text"])
        self.assertNotIn("password", payload)
        self.assertIn("access", payload)

    def test_order_entry_contains_public_url(self) -> None:
        payload = json.loads(mcp_server.get_order_entry()["content"][0]["text"])
        self.assertEqual(payload["provider"], "美团点餐")
        self.assertEqual(payload["order_url"], "https://rms.meituan.com/diancan/14/2HpfZPxOFw0")
        self.assertIn("二维码", payload["alternative_access"])

    def test_manifest_tools_match_server_tools(self) -> None:
        manifest = json.loads((PROJECT_ROOT / "skill.json").read_text(encoding="utf-8"))
        manifest_tools = {tool["name"] for tool in manifest["tools"]}
        self.assertSetEqual(manifest_tools, set(mcp_server.TOOLS))


if __name__ == "__main__":
    unittest.main()
