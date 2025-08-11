import program_2

def test_display_larger_than_n_list(capfd):
    testNumberList = [10, 5, 1]
    n = 6
    program_2.display_larger_than_n_list(n, testNumberList)
    out, err = capfd.readouterr()

    assert "10" in out