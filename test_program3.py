import program_3

def test_display_larger_than_n_list(capfd):
    user_input = [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    year_to_sum = 2010
    program_3.sum_population_for_year(user_input, year_to_sum)
    out, err = capfd.readouterr()

    assert "8,860,637" in out or "8860637" in out