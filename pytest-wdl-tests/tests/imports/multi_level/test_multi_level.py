def test_multi_level(workflow_runner):
    """
    import file A, that imports file B, that imports file C that has a task
    """
    inputs = {
        "file_name" : "foo.txt"
    }
    outputs = {}
    workflow_runner("main.wdl", inputs, outputs)
