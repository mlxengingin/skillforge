---
name: wechat-miniprogram-virtual-pay
description: Personal WeChat mini program virtual payment checklist (tools category).
---

# 微信小程序个人虚拟支付接入清单

## When to use
Personal-subject mini program in 工具 category needs paid unlocks.

## Workflow
1. Confirm: personal subject + 工具 category + certified + ICP filed.
2. Open 虚拟支付 in MP; record AppID / OfferID / AppKey.
3. Implement goods purchase via wx.requestVirtualPayment.
4. Deploy deliver notify + query_order fallback (idempotent on wx_order_id).
5. Test Android (1% fee) path; note iOS 12% and version gate.

## Guardrails
- Monthly cap 100,000 CNY for personal subjects.
- Do not offer telecom-license-required services.
- Never treat frontend success callback as sole deliver proof.

