from pathlib import Path
import random
import os

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)
food_file = script_dir / "food.txt"

foods = ["滷肉飯", "火鍋", "披薩", "壽司", "牛肉麵"]

def load_favorites():
    if not food_file.exists():
        return[]
    with open(food_file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]
    
def save_favorite(food):
    with open(food_file, "a", encoding="utf-8") as file:
        file.write(f"{food}\n")
    print(f"已儲存: {food}")

def suggest_food():
    favorites = load_favorites()
    all_foods = foods + favorites
    return random.choice(all_foods) if all_foods else "沒食物，請加入！"

def main():
    print("決定吃什麼！")
    while True:
        print("\n指令: suggest/save/list/exit")
        cmd = input("請輸入指令:").strip().lower()
        if cmd == "exit":
            print("下次再來！")
            break
        elif cmd == "suggest":
            food = suggest_food()
            print(f"吃{food}吧！")
        elif cmd.startswith("save "):
            food = cmd[5:].strip()
            if food:
                save_favorite(food)
            else:
                print("食物不能空白")
        elif cmd == "list":
            favorites = load_favorites()
            if favorites:
                print("你的最愛:")
                for i, food in enumerate(favorites, 1):
                    print(f"{i}.{food}")
            else:
                print("還沒有最愛喔！快加入吧！")
        else:
            print("無效指令")

if __name__ == "__main__":
    main()