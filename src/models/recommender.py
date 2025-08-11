def score_example(roi: float, rent_growth: float, sentiment: float, w=(0.5,0.3,0.2)):
    s = w[0]*roi + w[1]*rent_growth + w[2]*sentiment
    if s >= 0.6: return "BUY", s
    if s >= 0.45: return "HOLD", s
    return "SELL", s