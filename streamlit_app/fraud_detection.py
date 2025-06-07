def predict_fraud(transaction):
    amount = transaction.get("amount", 0)
    merchant = transaction.get("merchant", "").lower()
    location = transaction.get("location", "").lower()
    time = transaction.get("time", 12)
    transaction_type = transaction.get("type", "").lower()
    device = transaction.get("device", "").lower()
    upi_id = transaction.get("upi_id", "").lower()
    failed_attempts = transaction.get("failed_attempts", 0)
    time_gap = transaction.get("time_gap", 999)

    if amount > 50000:
        return True
    if any(k in merchant for k in ["lottery", "crypto", "bet", "gamble", "casino", "nigerian", "scam"]):
        return True
    if time < 6 or time > 22:
        return True
    if any(loc in location for loc in ["nigeria", "north korea", "syria"]):
        return True
    if transaction_type in ["pull", "credit"] and "unknown" in merchant:
        return True
    if "rooted" in device or "jailbroken" in device:
        return True
    if any(k in upi_id for k in ["fraud", "fake", "test", "trial", "0000"]):
        return True
    if failed_attempts > 3:
        return True
    if time_gap < 5:
        return True

    return False
