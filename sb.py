def create_data_dict(tic_exchange_dic, tickers_lst, col_lst):
    data_dict = {}
    for ticker in tickers_lst:
        exchange = tic_exchange_dic[ticker]
        data = []
        with open(f"{ticker}.dat", "r") as f:
            lines = f.readlines()[1:]  # skip header
            for line in lines:
                fields = line.strip().split(",")
                row_dict = {col: val for col, val in zip(col_lst, fields) if col in col_lst}
                data.append(row_dict)
        data_dict[ticker] = {"exchange": exchange, "data": data}
    return data_dict

def create_data_dict(tic_exchange_dic, tickers_lst, col_lst):
    dict = {}
    for ticker in tickers_lst:
        exchange = tic_exchange_dic[ticker]
        if tickers_lst is None:
        tickers_lst = list(tic_exchange_dic.keys())

        with open(f"{ticker}.dat", "r") as f:
            lines = f.readlines()
            for line in lines:
                fields = line.strip().split(",")
                data_dict = line_to_dict(line)
                dict[fields[0]] = fields[1:]
        dict[ticker] = {"exchange": exchange, "data": data}

    return dict

