import speedtest

def simulate_download_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    return st.results.ping

def main():
    print("Simulating internet speed...")
    ping_speed = simulate_download_speed()
    print(f"Your internet speed is approximately {ping_speed} ms")

if __name__ == "__main__":
    main()
