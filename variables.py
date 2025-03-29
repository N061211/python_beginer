
"""
🚀 題目：Ammo Reload Simulator（彈藥補充模擬器）
你正在開發一款射擊遊戲的模擬系統。

玩家有以下設定：

初始子彈數：current_ammo（單一彈匣最多為 magazine_capacity）

背包中的子彈總數：total_reserve_ammo

每次補彈會把彈匣補滿（如果背包子彈夠）
"""

# function
def reload_ammo(current_ammo: str, total_reserve_ammo: int, magazine_capacity: int) -> tuple:
    """
    模擬補彈過程，回傳補彈後的 (current_ammo, total_reserve_ammo)
    """
    # 實作邏輯...
    

reload_ammo(5, 30, 10) 
# 彈匣最多 10 顆，現在有 5 顆 → 需要補 5 顆 → 從 reserve 扣 5 顆
# 輸出: (10, 25)

reload_ammo(10, 100, 10)
# 已滿，不需要補
# 輸出: (10, 100)

reload_ammo(3, 2, 10)
# 需要補 7 顆，但 reserve 只有 2 顆 → 補到 5 顆
# 輸出: (5, 0)
def reload_ammo(current_ammo: int, total_reserve_ammo: int, magazine_capacity: int) -> tuple:
    missing = magazine_capacity - current_ammo
    bullets_to_reload = min(missing, total_reserve_ammo)
    
    current_ammo += bullets_to_reload
    total_reserve_ammo -= bullets_to_reload

    return current_ammo, total_reserve_ammo

# 測試案例 1
result = reload_ammo(5, 30, 10)
assert result == (10, 25), f"Test 1 Failed: got {result}, expected (10, 25)"
print("✅ Test 1 Passed")

# 測試案例 2
result = reload_ammo(10, 100, 10)
assert result == (10, 100), f"Test 2 Failed: got {result}, expected (10, 100)"
print("✅ Test 2 Passed")

# 測試案例 3
result = reload_ammo(3, 2, 10)
assert result == (5, 0), f"Test 3 Failed: got {result}, expected (5, 0)"
print("✅ Test 3 Passed")

# 你也可以加更多測試看看
