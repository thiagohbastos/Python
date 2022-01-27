#%%
def teste(num: int = 5, itens: list() = [1, 2, 3]) -> int:
    for cont in range(0, len(itens)):
        itens[cont] *= num
        itens[cont] = str(itens[cont])
    itens = "|".join(itens)
    return itens

# %%
print(teste())
# %%
