import time
import random

class GasThrottler:
    def __init__(self, gas_limit: int = 150_000):
        self.gas_limit = gas_limit
        self.throttled_tx = []

    def simulate_incoming_tx(self):
        """Simulates incoming tx with random gas usage"""
        return {
            "tx_hash": f"0x{random.getrandbits(256):064x}",
            "gas": random.randint(20_000, 250_000),
            "timestamp": time.time()
        }

    def check_tx(self, tx):
        if tx["gas"] > self.gas_limit:
            self.throttled_tx.append(tx)
            print(f"[!] Throttled TX: {tx['tx_hash']} (Gas: {tx['gas']})")
            return False
        else:
            print(f"[✓] Accepted TX: {tx['tx_hash']} (Gas: {tx['gas']})")
            return True

    def run(self, rounds=10, delay=1.0):
        for _ in range(rounds):
            tx = self.simulate_incoming_tx()
            self.check_tx(tx)
            time.sleep(delay)

if __name__ == "__main__":
    print("🚦 Starting Gas Throttler")
    throttler = GasThrottler(gas_limit=120_000)
    throttler.run()
