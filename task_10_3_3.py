text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {sym: text.count(sym) for sym in set(text)}

print(*result.items())
