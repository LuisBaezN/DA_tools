# renombra las columnas
def rename_cols(cols: list, new_names: list = [], new_names_indx: list = [], space_size: int = 7) -> list:
    '''
    Changes the columns names to the snake standard. You can provide a list of names to spicify a custom name using
    the `new_names` parameter and then using the `new_names_indx` parameter to link the desired name index.
    '''

    if len(new_names_indx) != len(new_names):
        raise ValueError().add_note('> Lists have different sizes')

    new_columns: list = []
    word: str = ''

    for name in cols:
        word = name.strip()
        word = word.lower()
        for i in range(space_size, 0, -1):
            word = word.replace(' '*i, '_')

        new_columns.append(word)

    if len(new_names) > 0:
        cont: int = 0
        for i in new_names_indx:
             new_columns[i] = new_names[cont]
             cont += 1
    
    return new_columns


if __name__ == '__main__':
    columnas = ['asdA as dS', 'ASd dsa', ' aw as as  asaA   a']

    
    print(rename_cols(columnas, new_names=['test'], new_names_indx=[1], ))