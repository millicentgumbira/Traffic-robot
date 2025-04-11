import time

def show_light(color: str, duration: int):
    print(f"{color.upper()} light is ON for {duration} seconds")
    time.sleep(duration)
    print(f"{color.upper()} light is OFF/n")

def traffic_light_cycle():
    while True:
        show_light("amber", 5)
        show_light("red", 10)
        show_light("green", 20)

if __name__ == "__main__":
    try:
        traffic_light_cycle()
    except KeyboardInterrupt:
        print("\nTraffic light simulation stopped.")