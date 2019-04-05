import HW4.task3.trades_logic as logic

transactions, market_list = logic.initarr('trades.csv')

(main_window_start, main_window_len,
 main_window_sum, main_window_start_time) = logic.longest_window(transactions)

division = logic.dividing_window_by_markets(transactions, market_list,
                                            main_window_start,
                                            main_window_len)

windows_by_markets = logic.longest_windows_by_markets(transactions,
                                                      market_list)
print("Главное окно")
print(main_window_start_time, main_window_len, main_window_sum)
print("Разделение главного окна по биржам")
for div in division:
    print(div)
print("Разделение транзакций по биржам")
for window in windows_by_markets:
    print(window)
