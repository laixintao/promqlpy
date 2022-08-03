from promqlpy import split_binary_op


def test_case_0():
    assert split_binary_op("pg_up == 0") == {
        "code": "pg_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pg_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_1():
    assert split_binary_op(
        "time() - pg_postmaster_start_time_seconds < 60"
    ) == {
        "code": "(time() - pg_postmaster_start_time_seconds) < 60",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "time() - pg_postmaster_start_time_seconds",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "60",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_2():
    assert split_binary_op("pg_exporter_last_scrape_error > 0") == {
        "code": "pg_exporter_last_scrape_error > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pg_exporter_last_scrape_error",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_3():
    assert split_binary_op(
        "pg_replication_lag > 30 and ON(instance) pg_replication_is_replica == 1"
    ) == {
        "code": "(pg_replication_lag > 30) and on (instance) "
        "(pg_replication_is_replica == 1)",
        "group_modifier": {"args": ["instance"], "op": "on"},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pg_replication_lag > 30",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "pg_replication_lag",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "30",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "pg_replication_is_replica == 1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "pg_replication_is_replica",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "1",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_4():
    assert split_binary_op(
        "(pg_stat_user_tables_last_autovacuum > 0) and (time() - pg_stat_user_tables_last_autovacuum) > 60 * 60 * 24 * 10"
    ) == {
        "code": "(pg_stat_user_tables_last_autovacuum > 0) and ((time() - "
        "pg_stat_user_tables_last_autovacuum) > 864000)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pg_stat_user_tables_last_autovacuum > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "pg_stat_user_tables_last_autovacuum",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "(time() - pg_stat_user_tables_last_autovacuum) > "
            "864000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "time() - " "pg_stat_user_tables_last_autovacuum",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "864000",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_5():
    assert split_binary_op(
        "(pg_stat_user_tables_last_autoanalyze > 0) and (time() - pg_stat_user_tables_last_autoanalyze) > 24 * 60 * 60 * 10"
    ) == {
        "code": "(pg_stat_user_tables_last_autoanalyze > 0) and ((time() - "
        "pg_stat_user_tables_last_autoanalyze) > 864000)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pg_stat_user_tables_last_autoanalyze > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "pg_stat_user_tables_last_autoanalyze",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "(time() - pg_stat_user_tables_last_autoanalyze) > "
            "864000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "time() - " "pg_stat_user_tables_last_autoanalyze",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "864000",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_6():
    assert split_binary_op(
        'sum by (datname) (pg_stat_activity_count{datname!~"template.*|postgres"}) > pg_settings_max_connections * 0.8'
    ) == {
        "code": 'sum(pg_stat_activity_count{datname!~"template.*|postgres"}) by '
        "(datname) > (pg_settings_max_connections * 0.8)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(pg_stat_activity_count{datname!~"template.*|postgres"}) '
            "by (datname)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "pg_settings_max_connections * 0.8",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_7():
    assert split_binary_op(
        'sum by (datname) (pg_stat_activity_count{datname!~"template.*|postgres"}) < 5'
    ) == {
        "code": 'sum(pg_stat_activity_count{datname!~"template.*|postgres"}) by '
        "(datname) < 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(pg_stat_activity_count{datname!~"template.*|postgres"}) '
            "by (datname)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_8():
    assert split_binary_op(
        'increase(pg_stat_database_deadlocks{datname!~"template.*|postgres"}[1m]) > 5'
    ) == {
        "code": 'increase(pg_stat_database_deadlocks{datname!~"template.*|postgres"}[1m]) '
        "> 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(pg_stat_database_deadlocks{datname!~"template.*|postgres"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_9():
    assert split_binary_op(
        'rate(pg_stat_database_xact_rollback{datname!~"template.*"}[3m]) / rate(pg_stat_database_xact_commit{datname!~"template.*"}[3m]) > 0.02'
    ) == {
        "code": '(rate(pg_stat_database_xact_rollback{datname!~"template.*"}[3m]) '
        '/ rate(pg_stat_database_xact_commit{datname!~"template.*"}[3m])) '
        "> 0.02",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rate(pg_stat_database_xact_rollback{datname!~"template.*"}[3m]) '
            "/ "
            'rate(pg_stat_database_xact_commit{datname!~"template.*"}[3m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.02",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_10():
    assert split_binary_op("rate(pg_stat_database_xact_commit[1m]) < 10") == {
        "code": "rate(pg_stat_database_xact_commit[1m]) < 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(pg_stat_database_xact_commit[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_11():
    assert split_binary_op("rate(pg_txid_current[1m]) < 5") == {
        "code": "rate(pg_txid_current[1m]) < 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(pg_txid_current[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_12():
    assert split_binary_op(
        'rate(postgresql_errors_total{type="statement_timeout"}[1m]) > 3'
    ) == {
        "code": 'rate(postgresql_errors_total{type="statement_timeout"}[1m]) > 3',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rate(postgresql_errors_total{type="statement_timeout"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_13():
    assert split_binary_op(
        'increase(postgresql_errors_total{type="deadlock_detected"}[1m]) > 1'
    ) == {
        "code": 'increase(postgresql_errors_total{type="deadlock_detected"}[1m]) > '
        "1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(postgresql_errors_total{type="deadlock_detected"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_14():
    assert split_binary_op("pg_replication_slots_active == 0") == {
        "code": "pg_replication_slots_active == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pg_replication_slots_active",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_15():
    assert split_binary_op(
        "((pg_stat_user_tables_n_dead_tup > 10000) / (pg_stat_user_tables_n_live_tup + pg_stat_user_tables_n_dead_tup)) >= 0.1 unless ON(instance) (pg_replication_is_replica == 1)"
    ) == {
        "code": "(((pg_stat_user_tables_n_dead_tup > 10000) / "
        "(pg_stat_user_tables_n_live_tup + "
        "pg_stat_user_tables_n_dead_tup)) >= 0.1) unless on (instance) "
        "(pg_replication_is_replica == 1)",
        "group_modifier": {"args": ["instance"], "op": "on"},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "((pg_stat_user_tables_n_dead_tup > 10000) / "
            "(pg_stat_user_tables_n_live_tup + "
            "pg_stat_user_tables_n_dead_tup)) >= 0.1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "(pg_stat_user_tables_n_dead_tup > 10000) "
                "/ (pg_stat_user_tables_n_live_tup + "
                "pg_stat_user_tables_n_dead_tup)",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">=",
            "right": {
                "code": "0.1",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "unless",
        "right": {
            "code": "pg_replication_is_replica == 1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "pg_replication_is_replica",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "1",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_16():
    assert split_binary_op("count(pg_replication_is_replica == 0) != 1") == {
        "code": "count(pg_replication_is_replica == 0) != 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "count(pg_replication_is_replica == 0)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_17():
    assert split_binary_op(
        "pg_replication_is_replica and changes(pg_replication_is_replica[1m]) > 0"
    ) == {
        "code": "pg_replication_is_replica and "
        "(changes(pg_replication_is_replica[1m]) > 0)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pg_replication_is_replica",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "and",
        "right": {
            "code": "changes(pg_replication_is_replica[1m]) > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "changes(pg_replication_is_replica[1m])",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_18():
    assert split_binary_op(
        '{__name__=~"pg_settings_.*"} != ON(__name__) {__name__=~"pg_settings_([^t]|t[^r]|tr[^a]|tra[^n]|tran[^s]|trans[^a]|transa[^c]|transac[^t]|transact[^i]|transacti[^o]|transactio[^n]|transaction[^_]|transaction_[^r]|transaction_r[^e]|transaction_re[^a]|transaction_rea[^d]|transaction_read[^_]|transaction_read_[^o]|transaction_read_o[^n]|transaction_read_on[^l]|transaction_read_onl[^y]).*"} OFFSET 5m'
    ) == {
        "code": '{__name__=~"pg_settings_.*"} != on (__name__) '
        '{__name__=~"pg_settings_([^t]|t[^r]|tr[^a]|tra[^n]|tran[^s]|trans[^a]|transa[^c]|transac[^t]|transact[^i]|transacti[^o]|transactio[^n]|transaction[^_]|transaction_[^r]|transaction_r[^e]|transaction_re[^a]|transaction_rea[^d]|transaction_read[^_]|transaction_read_[^o]|transaction_read_o[^n]|transaction_read_on[^l]|transaction_read_onl[^y]).*"} '
        "offset 5m",
        "group_modifier": {"args": ["__name__"], "op": "on"},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '{__name__=~"pg_settings_.*"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": '{__name__=~"pg_settings_([^t]|t[^r]|tr[^a]|tra[^n]|tran[^s]|trans[^a]|transa[^c]|transac[^t]|transact[^i]|transacti[^o]|transactio[^n]|transaction[^_]|transaction_[^r]|transaction_r[^e]|transaction_re[^a]|transaction_rea[^d]|transaction_read[^_]|transaction_read_[^o]|transaction_read_o[^n]|transaction_read_on[^l]|transaction_read_onl[^y]).*"} '
            "offset 5m",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_19():
    assert split_binary_op("sum(pg_stat_ssl_compression) > 0") == {
        "code": "sum(pg_stat_ssl_compression) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(pg_stat_ssl_compression)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_20():
    assert split_binary_op(
        "((sum (pg_locks_count)) / (pg_settings_max_locks_per_transaction * pg_settings_max_connections)) > 0.20"
    ) == {
        "code": "(sum(pg_locks_count) / (pg_settings_max_locks_per_transaction * "
        "pg_settings_max_connections)) > 0.2",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(pg_locks_count) / "
            "(pg_settings_max_locks_per_transaction * "
            "pg_settings_max_connections)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_21():
    assert split_binary_op(
        "pg_bloat_btree_bloat_pct > 80 and on (idxname) (pg_bloat_btree_real_size > 100000000)"
    ) == {
        "code": "(pg_bloat_btree_bloat_pct > 80) and on (idxname) "
        "(pg_bloat_btree_real_size > 1e+08)",
        "group_modifier": {"args": ["idxname"], "op": "on"},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pg_bloat_btree_bloat_pct > 80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "pg_bloat_btree_bloat_pct",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "80",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "pg_bloat_btree_real_size > 1e+08",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "pg_bloat_btree_real_size",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "1e+08",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_22():
    assert split_binary_op(
        "pg_bloat_table_bloat_pct > 80 and on (relname) (pg_bloat_table_real_size > 200000000)"
    ) == {
        "code": "(pg_bloat_table_bloat_pct > 80) and on (relname) "
        "(pg_bloat_table_real_size > 2e+08)",
        "group_modifier": {"args": ["relname"], "op": "on"},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pg_bloat_table_bloat_pct > 80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "pg_bloat_table_bloat_pct",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "80",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "pg_bloat_table_real_size > 2e+08",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "pg_bloat_table_real_size",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "2e+08",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_23():
    assert split_binary_op(
        'changes(process_start_time_seconds{job=~"loki"}[15m]) > 2'
    ) == {
        "code": 'changes(process_start_time_seconds{job=~"loki"}[15m]) > 2',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'changes(process_start_time_seconds{job=~"loki"}[15m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_24():
    assert split_binary_op(
        '100 * sum(rate(loki_request_duration_seconds_count{status_code=~"5.."}[1m])) by (namespace, job, route) / sum(rate(loki_request_duration_seconds_count[1m])) by (namespace, job, route) > 10'
    ) == {
        "code": "((100 * "
        'sum(rate(loki_request_duration_seconds_count{status_code=~"5.."}[1m])) '
        "by (namespace, job, route)) / "
        "sum(rate(loki_request_duration_seconds_count[1m])) by (namespace, "
        "job, route)) > 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(100 * "
            'sum(rate(loki_request_duration_seconds_count{status_code=~"5.."}[1m])) '
            "by (namespace, job, route)) / "
            "sum(rate(loki_request_duration_seconds_count[1m])) by "
            "(namespace, job, route)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_25():
    assert split_binary_op(
        "sum(increase(loki_panic_total[10m])) by (namespace, job) > 0"
    ) == {
        "code": "sum(increase(loki_panic_total[10m])) by (namespace, job) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(increase(loki_panic_total[10m])) by (namespace, "
            "job)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_26():
    assert split_binary_op(
        '(histogram_quantile(0.99, sum(rate(loki_request_duration_seconds_bucket{route!~"(?i).*tail.*"}[5m])) by (le)))  > 1'
    ) == {
        "code": "histogram_quantile(0.99, "
        'sum(rate(loki_request_duration_seconds_bucket{route!~"(?i).*tail.*"}[5m])) '
        "by (le)) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            'sum(rate(loki_request_duration_seconds_bucket{route!~"(?i).*tail.*"}[5m])) '
            "by (le))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_27():
    assert split_binary_op(
        "cortex_ruler_config_last_reload_successful != 1"
    ) == {
        "code": "cortex_ruler_config_last_reload_successful != 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "cortex_ruler_config_last_reload_successful",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_28():
    assert split_binary_op(
        "cortex_prometheus_notifications_alertmanagers_discovered < 1"
    ) == {
        "code": "cortex_prometheus_notifications_alertmanagers_discovered < 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "cortex_prometheus_notifications_alertmanagers_discovered",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_29():
    assert split_binary_op(
        "rate(cortex_prometheus_notifications_dropped_total[5m]) > 0"
    ) == {
        "code": "rate(cortex_prometheus_notifications_dropped_total[5m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(cortex_prometheus_notifications_dropped_total[5m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_30():
    assert split_binary_op(
        "rate(cortex_prometheus_notifications_errors_total[5m]) > 0"
    ) == {
        "code": "rate(cortex_prometheus_notifications_errors_total[5m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(cortex_prometheus_notifications_errors_total[5m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_31():
    assert split_binary_op(
        'cortex_ring_members{state="Unhealthy", name="ingester"} > 0'
    ) == {
        "code": 'cortex_ring_members{state="Unhealthy", name="ingester"} > 0',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cortex_ring_members{state="Unhealthy", '
            'name="ingester"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_32():
    assert split_binary_op(
        "sum by (job) (cortex_query_frontend_queue_length) > 0"
    ) == {
        "code": "sum(cortex_query_frontend_queue_length) by (job) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(cortex_query_frontend_queue_length) by (job)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_33():
    assert split_binary_op("ssl_probe_success == 0") == {
        "code": "ssl_probe_success == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ssl_probe_success",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_34():
    assert split_binary_op("ssl_ocsp_response_status == 2") == {
        "code": "ssl_ocsp_response_status == 2",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ssl_ocsp_response_status",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_35():
    assert split_binary_op("ssl_ocsp_response_status == 1") == {
        "code": "ssl_ocsp_response_status == 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ssl_ocsp_response_status",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_36():
    assert split_binary_op(
        'ssl_verified_cert_not_after{chain_no="0"} - time() < 86400 * 7'
    ) == {
        "code": '(ssl_verified_cert_not_after{chain_no="0"} - time()) < 604800',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'ssl_verified_cert_not_after{chain_no="0"} - time()',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "604800",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_37():
    assert split_binary_op("vault_core_unsealed == 0") == {
        "code": "vault_core_unsealed == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "vault_core_unsealed",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_38():
    assert split_binary_op(
        "avg(vault_token_create_count - vault_token_store_count) > 0"
    ) == {
        "code": "avg(vault_token_create_count - vault_token_store_count) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "avg(vault_token_create_count - "
            "vault_token_store_count)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_39():
    assert split_binary_op(
        'vault_token_count_by_ttl{creation_ttl="+Inf"} > 3'
    ) == {
        "code": 'vault_token_count_by_ttl{creation_ttl="+Inf"} > 3',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'vault_token_count_by_ttl{creation_ttl="+Inf"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_40():
    assert split_binary_op(
        'rate(netdata_cpu_cpu_percentage_average{dimension="idle"}[1m]) > 80'
    ) == {
        "code": 'rate(netdata_cpu_cpu_percentage_average{dimension="idle"}[1m]) > '
        "80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rate(netdata_cpu_cpu_percentage_average{dimension="idle"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_41():
    assert split_binary_op(
        'rate(netdata_cpu_cpu_percentage_average{dimension="steal"}[1m]) > 10'
    ) == {
        "code": 'rate(netdata_cpu_cpu_percentage_average{dimension="steal"}[1m]) > '
        "10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rate(netdata_cpu_cpu_percentage_average{dimension="steal"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_42():
    assert split_binary_op(
        '100 / netdata_system_ram_MB_average * netdata_system_ram_MB_average{dimension=~"free|cached"} < 20'
    ) == {
        "code": "((100 / netdata_system_ram_MB_average) * "
        'netdata_system_ram_MB_average{dimension=~"free|cached"}) < 20',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(100 / netdata_system_ram_MB_average) * "
            'netdata_system_ram_MB_average{dimension=~"free|cached"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "20",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_43():
    assert split_binary_op(
        '100 / netdata_disk_space_GB_average * netdata_disk_space_GB_average{dimension=~"avail|cached"} < 20'
    ) == {
        "code": "((100 / netdata_disk_space_GB_average) * "
        'netdata_disk_space_GB_average{dimension=~"avail|cached"}) < 20',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(100 / netdata_disk_space_GB_average) * "
            'netdata_disk_space_GB_average{dimension=~"avail|cached"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "20",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_44():
    assert split_binary_op(
        'predict_linear(netdata_disk_space_GB_average{dimension=~"avail|cached"}[3h], 24 * 3600) < 0'
    ) == {
        "code": 'predict_linear(netdata_disk_space_GB_average{dimension=~"avail|cached"}[3h], '
        "86400) < 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'predict_linear(netdata_disk_space_GB_average{dimension=~"avail|cached"}[3h], '
            "86400)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_45():
    assert split_binary_op(
        "netdata_md_mismatch_cnt_unsynchronized_blocks_average > 1024"
    ) == {
        "code": "netdata_md_mismatch_cnt_unsynchronized_blocks_average > 1024",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "netdata_md_mismatch_cnt_unsynchronized_blocks_average",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1024",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_46():
    assert split_binary_op(
        "increase(netdata_smartd_log_reallocated_sectors_count_sectors_average[1m]) > 0"
    ) == {
        "code": "increase(netdata_smartd_log_reallocated_sectors_count_sectors_average[1m]) "
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(netdata_smartd_log_reallocated_sectors_count_sectors_average[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_47():
    assert split_binary_op(
        "netdata_smartd_log_current_pending_sector_count_sectors_average > 0"
    ) == {
        "code": "netdata_smartd_log_current_pending_sector_count_sectors_average > "
        "0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "netdata_smartd_log_current_pending_sector_count_sectors_average",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_48():
    assert split_binary_op(
        "increase(netdata_smartd_log_offline_uncorrectable_sector_count_sectors_average[2m]) > 0"
    ) == {
        "code": "increase(netdata_smartd_log_offline_uncorrectable_sector_count_sectors_average[2m]) "
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(netdata_smartd_log_offline_uncorrectable_sector_count_sectors_average[2m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_49():
    assert split_binary_op("avg_over_time(speedtest_download[10m]) < 100") == {
        "code": "avg_over_time(speedtest_download[10m]) < 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "avg_over_time(speedtest_download[10m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_50():
    assert split_binary_op("avg_over_time(speedtest_upload[10m]) < 20") == {
        "code": "avg_over_time(speedtest_upload[10m]) < 20",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "avg_over_time(speedtest_upload[10m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "20",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_51():
    assert split_binary_op(
        "sum(phpfpm_max_children_reached_total) by (instance) > 0"
    ) == {
        "code": "sum(phpfpm_max_children_reached_total) by (instance) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(phpfpm_max_children_reached_total) by (instance)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_52():
    assert split_binary_op("sidekiq_queue_size > 100") == {
        "code": "sidekiq_queue_size > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sidekiq_queue_size",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_53():
    assert split_binary_op("max(sidekiq_queue_latency) > 60") == {
        "code": "max(sidekiq_queue_latency) > 60",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "max(sidekiq_queue_latency)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "60",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_54():
    assert split_binary_op("freeswitch_up == 0") == {
        "code": "freeswitch_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "freeswitch_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_55():
    assert split_binary_op(
        "(freeswitch_session_active * 100 / freeswitch_session_limit) > 80"
    ) == {
        "code": "((freeswitch_session_active * 100) / freeswitch_session_limit) > "
        "80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(freeswitch_session_active * 100) / "
            "freeswitch_session_limit",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_56():
    assert split_binary_op(
        "(freeswitch_session_active * 100 / freeswitch_session_limit) > 90"
    ) == {
        "code": "((freeswitch_session_active * 100) / freeswitch_session_limit) > "
        "90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(freeswitch_session_active * 100) / "
            "freeswitch_session_limit",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_57():
    assert split_binary_op(
        'min(kube_deployment_status_replicas_available{deployment="istio-ingressgateway", namespace="istio-system"}) without (instance, pod) < 2'
    ) == {
        "code": 'min(kube_deployment_status_replicas_available{deployment="istio-ingressgateway", '
        'namespace="istio-system"}) without (instance, pod) < 2',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'min(kube_deployment_status_replicas_available{deployment="istio-ingressgateway", '
            'namespace="istio-system"}) without (instance, pod)',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_58():
    assert split_binary_op(
        "sum(rate(pilot_xds_push_errors[1m])) / sum(rate(pilot_xds_pushes[1m])) * 100 > 5"
    ) == {
        "code": "((sum(rate(pilot_xds_push_errors[1m])) / "
        "sum(rate(pilot_xds_pushes[1m]))) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(sum(rate(pilot_xds_push_errors[1m])) / "
            "sum(rate(pilot_xds_pushes[1m]))) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_59():
    assert split_binary_op(
        'sum(rate(mixer_runtime_dispatches_total{adapter=~"prometheus"}[1m])) < 180'
    ) == {
        "code": 'sum(rate(mixer_runtime_dispatches_total{adapter=~"prometheus"}[1m])) '
        "< 180",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(mixer_runtime_dispatches_total{adapter=~"prometheus"}[1m]))',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "180",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_60():
    assert split_binary_op(
        'sum(rate(istio_requests_total{reporter="destination"}[5m])) > 1000'
    ) == {
        "code": 'sum(rate(istio_requests_total{reporter="destination"}[5m])) > '
        "1000",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(istio_requests_total{reporter="destination"}[5m]))',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_61():
    assert split_binary_op(
        'sum(rate(istio_requests_total{reporter="destination"}[5m])) < 100'
    ) == {
        "code": 'sum(rate(istio_requests_total{reporter="destination"}[5m])) < 100',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(istio_requests_total{reporter="destination"}[5m]))',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_62():
    assert split_binary_op(
        'sum(rate(istio_requests_total{reporter="destination", response_code=~"4.*"}[5m])) / sum(rate(istio_requests_total{reporter="destination"}[5m])) * 100 > 5'
    ) == {
        "code": '((sum(rate(istio_requests_total{reporter="destination", '
        'response_code=~"4.*"}[5m])) / '
        'sum(rate(istio_requests_total{reporter="destination"}[5m]))) * '
        "100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(istio_requests_total{reporter="destination", '
            'response_code=~"4.*"}[5m])) / '
            'sum(rate(istio_requests_total{reporter="destination"}[5m]))) '
            "* 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_63():
    assert split_binary_op(
        'sum(rate(istio_requests_total{reporter="destination", response_code=~"5.*"}[5m])) / sum(rate(istio_requests_total{reporter="destination"}[5m])) * 100 > 5'
    ) == {
        "code": '((sum(rate(istio_requests_total{reporter="destination", '
        'response_code=~"5.*"}[5m])) / '
        'sum(rate(istio_requests_total{reporter="destination"}[5m]))) * '
        "100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(istio_requests_total{reporter="destination", '
            'response_code=~"5.*"}[5m])) / '
            'sum(rate(istio_requests_total{reporter="destination"}[5m]))) '
            "* 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_64():
    assert split_binary_op(
        'rate(istio_request_duration_milliseconds_sum{reporter="destination"}[1m]) / rate(istio_request_duration_milliseconds_count{reporter="destination"}[1m]) > 100'
    ) == {
        "code": '(rate(istio_request_duration_milliseconds_sum{reporter="destination"}[1m]) '
        "/ "
        'rate(istio_request_duration_milliseconds_count{reporter="destination"}[1m])) '
        "> 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rate(istio_request_duration_milliseconds_sum{reporter="destination"}[1m]) '
            "/ "
            'rate(istio_request_duration_milliseconds_count{reporter="destination"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_65():
    assert split_binary_op(
        "histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket[1m])) by (destination_canonical_service, destination_workload_namespace, source_canonical_service, source_workload_namespace, le)) > 1"
    ) == {
        "code": "histogram_quantile(0.99, "
        "sum(rate(istio_request_duration_milliseconds_bucket[1m])) by "
        "(destination_canonical_service, destination_workload_namespace, "
        "source_canonical_service, source_workload_namespace, le)) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            "sum(rate(istio_request_duration_milliseconds_bucket[1m])) "
            "by (destination_canonical_service, "
            "destination_workload_namespace, "
            "source_canonical_service, source_workload_namespace, "
            "le))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_66():
    assert split_binary_op(
        "sum(rate(pilot_duplicate_envoy_clusters{}[5m])) > 0"
    ) == {
        "code": "sum(rate(pilot_duplicate_envoy_clusters[5m])) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(pilot_duplicate_envoy_clusters[5m]))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_67():
    assert split_binary_op("redis_up == 0") == {
        "code": "redis_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "redis_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_68():
    assert split_binary_op(
        '(count(redis_instance_info{role="master"}) or vector(0)) < 1'
    ) == {
        "is_binary_op": True,
        "left": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": 'count(redis_instance_info{role="master"}) or vector(0)',
        },
        "right": {
            "is_binary_op": False,
            "left": None,
            "right": None,
            "op": "",
            "group_modifier": {"op": "", "args": None},
            "join_modifier": {"op": "", "args": None},
            "code": "1",
        },
        "op": "<",
        "group_modifier": {"op": "", "args": None},
        "join_modifier": {"op": "", "args": None},
        "code": '(count(redis_instance_info{role="master"}) or vector(0)) < 1',
    }


def test_case_69():
    assert split_binary_op(
        'count(redis_instance_info{role="master"}) > 1'
    ) == {
        "code": 'count(redis_instance_info{role="master"}) > 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'count(redis_instance_info{role="master"})',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_70():
    assert split_binary_op(
        "count without (instance, job) (redis_connected_slaves) - sum without (instance, job) (redis_connected_slaves) - 1 > 1"
    ) == {
        "code": "((count(redis_connected_slaves) without (instance, job) - "
        "sum(redis_connected_slaves) without (instance, job)) - 1) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(count(redis_connected_slaves) without (instance, "
            "job) - sum(redis_connected_slaves) without (instance, "
            "job)) - 1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_71():
    assert split_binary_op("delta(redis_connected_slaves[1m]) < 0") == {
        "code": "delta(redis_connected_slaves[1m]) < 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "delta(redis_connected_slaves[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_72():
    assert split_binary_op("changes(redis_connected_slaves[1m]) > 1") == {
        "code": "changes(redis_connected_slaves[1m]) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "changes(redis_connected_slaves[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_73():
    assert split_binary_op(
        "time() - redis_rdb_last_save_timestamp_seconds > 60 * 60 * 24"
    ) == {
        "code": "(time() - redis_rdb_last_save_timestamp_seconds) > 86400",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "time() - redis_rdb_last_save_timestamp_seconds",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "86400",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_74():
    assert split_binary_op(
        "redis_memory_used_bytes / redis_total_system_memory_bytes * 100 > 90"
    ) == {
        "code": "((redis_memory_used_bytes / redis_total_system_memory_bytes) * "
        "100) > 90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(redis_memory_used_bytes / "
            "redis_total_system_memory_bytes) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_75():
    assert split_binary_op(
        "redis_memory_used_bytes / redis_memory_max_bytes * 100 > 90"
    ) == {
        "code": "((redis_memory_used_bytes / redis_memory_max_bytes) * 100) > 90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(redis_memory_used_bytes / redis_memory_max_bytes) * "
            "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_76():
    assert split_binary_op("redis_connected_clients > 100") == {
        "code": "redis_connected_clients > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "redis_connected_clients",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_77():
    assert split_binary_op("redis_connected_clients < 5") == {
        "code": "redis_connected_clients < 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "redis_connected_clients",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_78():
    assert split_binary_op(
        "increase(redis_rejected_connections_total[1m]) > 0"
    ) == {
        "code": "increase(redis_rejected_connections_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(redis_rejected_connections_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_79():
    assert split_binary_op("ceph_health_status != 0") == {
        "code": "ceph_health_status != 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_health_status",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_80():
    assert split_binary_op("abs(ceph_monitor_clock_skew_seconds) > 0.2") == {
        "code": "abs(ceph_monitor_clock_skew_seconds) > 0.2",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "abs(ceph_monitor_clock_skew_seconds)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_81():
    assert split_binary_op("ceph_monitor_avail_percent < 10") == {
        "code": "ceph_monitor_avail_percent < 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_monitor_avail_percent",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_82():
    assert split_binary_op("ceph_osd_up == 0") == {
        "code": "ceph_osd_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_osd_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_83():
    assert split_binary_op("ceph_osd_perf_apply_latency_seconds > 5") == {
        "code": "ceph_osd_perf_apply_latency_seconds > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_osd_perf_apply_latency_seconds",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_84():
    assert split_binary_op("ceph_osd_utilization > 90") == {
        "code": "ceph_osd_utilization > 90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_osd_utilization",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_85():
    assert split_binary_op("ceph_osd_weight < 1") == {
        "code": "ceph_osd_weight < 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_osd_weight",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_86():
    assert split_binary_op("ceph_pg_down > 0") == {
        "code": "ceph_pg_down > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_pg_down",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_87():
    assert split_binary_op("ceph_pg_incomplete > 0") == {
        "code": "ceph_pg_incomplete > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_pg_incomplete",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_88():
    assert split_binary_op("ceph_pg_inconsistent > 0") == {
        "code": "ceph_pg_inconsistent > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_pg_inconsistent",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_89():
    assert split_binary_op("ceph_pg_activating > 0") == {
        "code": "ceph_pg_activating > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_pg_activating",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_90():
    assert split_binary_op("ceph_pg_backfill_toofull > 0") == {
        "code": "ceph_pg_backfill_toofull > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_pg_backfill_toofull",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_91():
    assert split_binary_op("ceph_pg_total - ceph_pg_active > 0") == {
        "code": "(ceph_pg_total - ceph_pg_active) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "ceph_pg_total - ceph_pg_active",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_92():
    assert split_binary_op("openebs_used_pool_capacity_percent > 80") == {
        "code": "openebs_used_pool_capacity_percent > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "openebs_used_pool_capacity_percent",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_93():
    assert split_binary_op('absent(up{job="prometheus"})') == {
        "code": 'absent(up{job="prometheus"})',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_94():
    assert split_binary_op("up == 0") == {
        "code": "up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_95():
    assert split_binary_op("sum by (job) (up) == 0") == {
        "code": "sum(up) by (job) == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(up) by (job)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_96():
    assert split_binary_op(
        "prometheus_config_last_reload_successful != 1"
    ) == {
        "code": "prometheus_config_last_reload_successful != 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "prometheus_config_last_reload_successful",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_97():
    assert split_binary_op(
        'changes(process_start_time_seconds{job=~"prometheus|pushgateway|alertmanager"}[15m]) > 2'
    ) == {
        "code": 'changes(process_start_time_seconds{job=~"prometheus|pushgateway|alertmanager"}[15m]) '
        "> 2",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'changes(process_start_time_seconds{job=~"prometheus|pushgateway|alertmanager"}[15m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_98():
    assert split_binary_op('absent(up{job="alertmanager"})') == {
        "code": 'absent(up{job="alertmanager"})',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_99():
    assert split_binary_op(
        "alertmanager_config_last_reload_successful != 1"
    ) == {
        "code": "alertmanager_config_last_reload_successful != 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "alertmanager_config_last_reload_successful",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_100():
    assert split_binary_op(
        'count(count_values("config_hash", alertmanager_config_hash)) > 1'
    ) == {
        "code": 'count(count_values("config_hash", alertmanager_config_hash)) > 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'count(count_values("config_hash", '
            "alertmanager_config_hash))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_101():
    assert split_binary_op("vector(1)") == {
        "code": "vector(1)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_102():
    assert split_binary_op(
        "prometheus_notifications_alertmanagers_discovered < 1"
    ) == {
        "code": "prometheus_notifications_alertmanagers_discovered < 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "prometheus_notifications_alertmanagers_discovered",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_103():
    assert split_binary_op(
        "increase(prometheus_rule_evaluation_failures_total[3m]) > 0"
    ) == {
        "code": "increase(prometheus_rule_evaluation_failures_total[3m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_rule_evaluation_failures_total[3m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_104():
    assert split_binary_op(
        "increase(prometheus_template_text_expansion_failures_total[3m]) > 0"
    ) == {
        "code": "increase(prometheus_template_text_expansion_failures_total[3m]) > "
        "0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_template_text_expansion_failures_total[3m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_105():
    assert split_binary_op(
        "prometheus_rule_group_last_duration_seconds > prometheus_rule_group_interval_seconds"
    ) == {
        "code": "prometheus_rule_group_last_duration_seconds > "
        "prometheus_rule_group_interval_seconds",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "prometheus_rule_group_last_duration_seconds",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "prometheus_rule_group_interval_seconds",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_106():
    assert split_binary_op(
        "min_over_time(prometheus_notifications_queue_length[10m]) > 0"
    ) == {
        "code": "min_over_time(prometheus_notifications_queue_length[10m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "min_over_time(prometheus_notifications_queue_length[10m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_107():
    assert split_binary_op(
        "rate(alertmanager_notifications_failed_total[1m]) > 0"
    ) == {
        "code": "rate(alertmanager_notifications_failed_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(alertmanager_notifications_failed_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_108():
    assert split_binary_op("prometheus_sd_discovered_targets == 0") == {
        "code": "prometheus_sd_discovered_targets == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "prometheus_sd_discovered_targets",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_109():
    assert split_binary_op(
        'prometheus_target_interval_length_seconds{quantile="0.9"} / on (interval, instance, job) prometheus_target_interval_length_seconds{quantile="0.5"} > 1.05'
    ) == {
        "code": '(prometheus_target_interval_length_seconds{quantile="0.9"} / on '
        "(interval, instance, job) "
        'prometheus_target_interval_length_seconds{quantile="0.5"}) > 1.05',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'prometheus_target_interval_length_seconds{quantile="0.9"} '
            "/ on (interval, instance, job) "
            'prometheus_target_interval_length_seconds{quantile="0.5"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1.05",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_110():
    assert split_binary_op(
        "increase(prometheus_target_scrapes_exceeded_sample_limit_total[10m]) > 10"
    ) == {
        "code": "increase(prometheus_target_scrapes_exceeded_sample_limit_total[10m]) "
        "> 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_target_scrapes_exceeded_sample_limit_total[10m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_111():
    assert split_binary_op(
        "increase(prometheus_target_scrapes_sample_duplicate_timestamp_total[5m]) > 0"
    ) == {
        "code": "increase(prometheus_target_scrapes_sample_duplicate_timestamp_total[5m]) "
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_target_scrapes_sample_duplicate_timestamp_total[5m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_112():
    assert split_binary_op(
        "increase(prometheus_tsdb_checkpoint_creations_failed_total[1m]) > 0"
    ) == {
        "code": "increase(prometheus_tsdb_checkpoint_creations_failed_total[1m]) > "
        "0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_tsdb_checkpoint_creations_failed_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_113():
    assert split_binary_op(
        "increase(prometheus_tsdb_checkpoint_deletions_failed_total[1m]) > 0"
    ) == {
        "code": "increase(prometheus_tsdb_checkpoint_deletions_failed_total[1m]) > "
        "0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_tsdb_checkpoint_deletions_failed_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_114():
    assert split_binary_op(
        "increase(prometheus_tsdb_compactions_failed_total[1m]) > 0"
    ) == {
        "code": "increase(prometheus_tsdb_compactions_failed_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_tsdb_compactions_failed_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_115():
    assert split_binary_op(
        "increase(prometheus_tsdb_head_truncations_failed_total[1m]) > 0"
    ) == {
        "code": "increase(prometheus_tsdb_head_truncations_failed_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_tsdb_head_truncations_failed_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_116():
    assert split_binary_op(
        "increase(prometheus_tsdb_reloads_failures_total[1m]) > 0"
    ) == {
        "code": "increase(prometheus_tsdb_reloads_failures_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_tsdb_reloads_failures_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_117():
    assert split_binary_op(
        "increase(prometheus_tsdb_wal_corruptions_total[1m]) > 0"
    ) == {
        "code": "increase(prometheus_tsdb_wal_corruptions_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_tsdb_wal_corruptions_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_118():
    assert split_binary_op(
        "increase(prometheus_tsdb_wal_truncations_failed_total[1m]) > 0"
    ) == {
        "code": "increase(prometheus_tsdb_wal_truncations_failed_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(prometheus_tsdb_wal_truncations_failed_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_119():
    assert split_binary_op("probe_success == 0") == {
        "code": "probe_success == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "probe_success",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_120():
    assert split_binary_op(
        "blackbox_exporter_config_last_reload_successful != 1"
    ) == {
        "code": "blackbox_exporter_config_last_reload_successful != 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "blackbox_exporter_config_last_reload_successful",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_121():
    assert split_binary_op(
        "avg_over_time(probe_duration_seconds[1m]) > 1"
    ) == {
        "code": "avg_over_time(probe_duration_seconds[1m]) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "avg_over_time(probe_duration_seconds[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_122():
    assert split_binary_op(
        "probe_http_status_code <= 199 OR probe_http_status_code >= 400"
    ) == {
        "code": "(probe_http_status_code <= 199) or (probe_http_status_code >= "
        "400)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "probe_http_status_code <= 199",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "probe_http_status_code",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "<=",
            "right": {
                "code": "199",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "or",
        "right": {
            "code": "probe_http_status_code >= 400",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "probe_http_status_code",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">=",
            "right": {
                "code": "400",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_123():
    assert split_binary_op(
        "probe_ssl_earliest_cert_expiry - time() < 86400 * 30"
    ) == {
        "code": "(probe_ssl_earliest_cert_expiry - time()) < 2.592e+06",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "probe_ssl_earliest_cert_expiry - time()",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "2.592e+06",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_124():
    assert split_binary_op(
        "probe_ssl_earliest_cert_expiry - time() < 86400 * 3"
    ) == {
        "code": "(probe_ssl_earliest_cert_expiry - time()) < 259200",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "probe_ssl_earliest_cert_expiry - time()",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "259200",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_125():
    assert split_binary_op("probe_ssl_earliest_cert_expiry - time() <= 0") == {
        "code": "(probe_ssl_earliest_cert_expiry - time()) <= 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "probe_ssl_earliest_cert_expiry - time()",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<=",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_126():
    assert split_binary_op(
        "avg_over_time(probe_http_duration_seconds[1m]) > 1"
    ) == {
        "code": "avg_over_time(probe_http_duration_seconds[1m]) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "avg_over_time(probe_http_duration_seconds[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_127():
    assert split_binary_op(
        "avg_over_time(probe_icmp_duration_seconds[1m]) > 1"
    ) == {
        "code": "avg_over_time(probe_icmp_duration_seconds[1m]) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "avg_over_time(probe_icmp_duration_seconds[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_128():
    assert split_binary_op(
        '(sum by (instance)(jvm_memory_used_bytes{area="heap"}) / sum by (instance)(jvm_memory_max_bytes{area="heap"})) * 100 > 80'
    ) == {
        "code": '((sum(jvm_memory_used_bytes{area="heap"}) by (instance) / '
        'sum(jvm_memory_max_bytes{area="heap"}) by (instance)) * 100) > 80',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(jvm_memory_used_bytes{area="heap"}) by '
            '(instance) / sum(jvm_memory_max_bytes{area="heap"}) '
            "by (instance)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_129():
    assert split_binary_op(
        '100 * sum(rate(promtail_request_duration_seconds_count{status_code=~"5..|failed"}[1m])) by (namespace, job, route, instance) / sum(rate(promtail_request_duration_seconds_count[1m])) by (namespace, job, route, instance) > 10'
    ) == {
        "code": "((100 * "
        'sum(rate(promtail_request_duration_seconds_count{status_code=~"5..|failed"}[1m])) '
        "by (namespace, job, route, instance)) / "
        "sum(rate(promtail_request_duration_seconds_count[1m])) by "
        "(namespace, job, route, instance)) > 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(100 * "
            'sum(rate(promtail_request_duration_seconds_count{status_code=~"5..|failed"}[1m])) '
            "by (namespace, job, route, instance)) / "
            "sum(rate(promtail_request_duration_seconds_count[1m])) "
            "by (namespace, job, route, instance)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_130():
    assert split_binary_op(
        "histogram_quantile(0.99, sum(rate(promtail_request_duration_seconds_bucket[5m])) by (le)) > 1"
    ) == {
        "code": "histogram_quantile(0.99, "
        "sum(rate(promtail_request_duration_seconds_bucket[5m])) by (le)) "
        "> 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            "sum(rate(promtail_request_duration_seconds_bucket[5m])) "
            "by (le))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_131():
    assert split_binary_op("rabbitmq_up == 0") == {
        "code": "rabbitmq_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rabbitmq_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_132():
    assert split_binary_op("sum(rabbitmq_running) < 3") == {
        "code": "sum(rabbitmq_running) < 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rabbitmq_running)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_133():
    assert split_binary_op("rabbitmq_partitions > 0") == {
        "code": "rabbitmq_partitions > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rabbitmq_partitions",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_134():
    assert split_binary_op(
        "rabbitmq_node_mem_used / rabbitmq_node_mem_limit * 100 > 90"
    ) == {
        "code": "((rabbitmq_node_mem_used / rabbitmq_node_mem_limit) * 100) > 90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(rabbitmq_node_mem_used / rabbitmq_node_mem_limit) * "
            "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_135():
    assert split_binary_op("rabbitmq_connectionsTotal > 1000") == {
        "code": "rabbitmq_connectionsTotal > 1000",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rabbitmq_connectionsTotal",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_136():
    assert split_binary_op(
        'rabbitmq_queue_messages{queue="my-dead-letter-queue"} > 10'
    ) == {
        "code": 'rabbitmq_queue_messages{queue="my-dead-letter-queue"} > 10',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rabbitmq_queue_messages{queue="my-dead-letter-queue"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_137():
    assert split_binary_op(
        'rabbitmq_queue_messages_ready{queue="my-queue"} > 1000'
    ) == {
        "code": 'rabbitmq_queue_messages_ready{queue="my-queue"} > 1000',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rabbitmq_queue_messages_ready{queue="my-queue"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_138():
    assert split_binary_op(
        'time() - rabbitmq_queue_head_message_timestamp{queue="my-queue"} > 60'
    ) == {
        "code": "(time() - "
        'rabbitmq_queue_head_message_timestamp{queue="my-queue"}) > 60',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "time() - "
            'rabbitmq_queue_head_message_timestamp{queue="my-queue"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "60",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_139():
    assert split_binary_op("rabbitmq_queue_consumers == 0") == {
        "code": "rabbitmq_queue_consumers == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rabbitmq_queue_consumers",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_140():
    assert split_binary_op(
        'rabbitmq_queue_consumers{queue="my-queue"} > 1'
    ) == {
        "code": 'rabbitmq_queue_consumers{queue="my-queue"} > 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rabbitmq_queue_consumers{queue="my-queue"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_141():
    assert split_binary_op(
        'rate(rabbitmq_exchange_messages_published_in_total{exchange="my-exchange"}[1m]) < 5'
    ) == {
        "code": 'rate(rabbitmq_exchange_messages_published_in_total{exchange="my-exchange"}[1m]) '
        "< 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rate(rabbitmq_exchange_messages_published_in_total{exchange="my-exchange"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_142():
    assert split_binary_op("sum(rabbitmq_build_info) < 3") == {
        "code": "sum(rabbitmq_build_info) < 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rabbitmq_build_info)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_143():
    assert split_binary_op("erlang_vm_dist_node_state < 3") == {
        "code": "erlang_vm_dist_node_state < 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "erlang_vm_dist_node_state",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_144():
    assert split_binary_op(
        "count(count(rabbitmq_build_info) by (rabbitmq_version)) > 1"
    ) == {
        "code": "count(count(rabbitmq_build_info) by (rabbitmq_version)) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "count(count(rabbitmq_build_info) by "
            "(rabbitmq_version))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_145():
    assert split_binary_op(
        "rabbitmq_process_resident_memory_bytes / rabbitmq_resident_memory_limit_bytes * 100 > 90"
    ) == {
        "code": "((rabbitmq_process_resident_memory_bytes / "
        "rabbitmq_resident_memory_limit_bytes) * 100) > 90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(rabbitmq_process_resident_memory_bytes / "
            "rabbitmq_resident_memory_limit_bytes) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_146():
    assert split_binary_op(
        "rabbitmq_process_open_fds / rabbitmq_process_max_fds * 100 > 90"
    ) == {
        "code": "((rabbitmq_process_open_fds / rabbitmq_process_max_fds) * 100) > "
        "90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(rabbitmq_process_open_fds / "
            "rabbitmq_process_max_fds) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_147():
    assert split_binary_op(
        "sum(rabbitmq_queue_messages_unacked) BY (queue) > 1000"
    ) == {
        "code": "sum(rabbitmq_queue_messages_unacked) by (queue) > 1000",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rabbitmq_queue_messages_unacked) by (queue)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_148():
    assert split_binary_op("rabbitmq_connections > 1000") == {
        "code": "rabbitmq_connections > 1000",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rabbitmq_connections",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_149():
    assert split_binary_op("rabbitmq_queue_consumers < 1") == {
        "code": "rabbitmq_queue_consumers < 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rabbitmq_queue_consumers",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_150():
    assert split_binary_op(
        "increase(rabbitmq_channel_messages_unroutable_returned_total[1m]) > 0 or increase(rabbitmq_channel_messages_unroutable_dropped_total[1m]) > 0"
    ) == {
        "code": "(increase(rabbitmq_channel_messages_unroutable_returned_total[1m]) "
        "> 0) or "
        "(increase(rabbitmq_channel_messages_unroutable_dropped_total[1m]) "
        "> 0)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(rabbitmq_channel_messages_unroutable_returned_total[1m]) "
            "> 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "increase(rabbitmq_channel_messages_unroutable_returned_total[1m])",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "or",
        "right": {
            "code": "increase(rabbitmq_channel_messages_unroutable_dropped_total[1m]) "
            "> 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "increase(rabbitmq_channel_messages_unroutable_dropped_total[1m])",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_151():
    assert split_binary_op("minio_disks_offline > 0") == {
        "code": "minio_disks_offline > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "minio_disks_offline",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_152():
    assert split_binary_op(
        "disk_storage_available / disk_storage_total * 100 < 10"
    ) == {
        "code": "((disk_storage_available / disk_storage_total) * 100) < 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(disk_storage_available / disk_storage_total) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_153():
    assert split_binary_op(
        'changes(mgob_scheduler_backup_total{status="500"}[1h]) > 0'
    ) == {
        "code": 'changes(mgob_scheduler_backup_total{status="500"}[1h]) > 0',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'changes(mgob_scheduler_backup_total{status="500"}[1h])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_154():
    assert split_binary_op(
        'avg(mongodb_replset_member_optime_date{state="PRIMARY"}) - avg(mongodb_replset_member_optime_date{state="SECONDARY"}) > 10'
    ) == {
        "code": '(avg(mongodb_replset_member_optime_date{state="PRIMARY"}) - '
        'avg(mongodb_replset_member_optime_date{state="SECONDARY"})) > 10',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'avg(mongodb_replset_member_optime_date{state="PRIMARY"}) '
            "- "
            'avg(mongodb_replset_member_optime_date{state="SECONDARY"})',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_155():
    assert split_binary_op("mongodb_replset_member_state == 3") == {
        "code": "mongodb_replset_member_state == 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mongodb_replset_member_state",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_156():
    assert split_binary_op("mongodb_replset_member_state == 6") == {
        "code": "mongodb_replset_member_state == 6",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mongodb_replset_member_state",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "6",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_157():
    assert split_binary_op("mongodb_replset_member_state == 8") == {
        "code": "mongodb_replset_member_state == 8",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mongodb_replset_member_state",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "8",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_158():
    assert split_binary_op("mongodb_replset_member_state == 9") == {
        "code": "mongodb_replset_member_state == 9",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mongodb_replset_member_state",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "9",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_159():
    assert split_binary_op("mongodb_replset_member_state == 10") == {
        "code": "mongodb_replset_member_state == 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mongodb_replset_member_state",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_160():
    assert split_binary_op(
        'mongodb_metrics_cursor_open{state="total_open"} > 10000'
    ) == {
        "code": 'mongodb_metrics_cursor_open{state="total_open"} > 10000',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'mongodb_metrics_cursor_open{state="total_open"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_161():
    assert split_binary_op(
        "increase(mongodb_metrics_cursor_timed_out_total[1m]) > 100"
    ) == {
        "code": "increase(mongodb_metrics_cursor_timed_out_total[1m]) > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(mongodb_metrics_cursor_timed_out_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_162():
    assert split_binary_op(
        'avg by(instance) (rate(mongodb_connections{state="current"}[1m])) / avg by(instance) (sum (mongodb_connections) by (instance)) * 100 > 80'
    ) == {
        "code": '((avg(rate(mongodb_connections{state="current"}[1m])) by '
        "(instance) / avg(sum(mongodb_connections) by (instance)) by "
        "(instance)) * 100) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(avg(rate(mongodb_connections{state="current"}[1m])) '
            "by (instance) / avg(sum(mongodb_connections) by "
            "(instance)) by (instance)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_163():
    assert split_binary_op(
        '(sum(mongodb_memory{type="virtual"}) BY (instance) / sum(mongodb_memory{type="mapped"}) BY (instance)) > 3'
    ) == {
        "code": '(sum(mongodb_memory{type="virtual"}) by (instance) / '
        'sum(mongodb_memory{type="mapped"}) by (instance)) > 3',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(mongodb_memory{type="virtual"}) by (instance) / '
            'sum(mongodb_memory{type="mapped"}) by (instance)',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_164():
    assert split_binary_op("mongodb_up == 0") == {
        "code": "mongodb_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mongodb_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_165():
    assert split_binary_op("mongodb_rs_members_health == 0") == {
        "code": "mongodb_rs_members_health == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mongodb_rs_members_health",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_166():
    assert split_binary_op(
        'mongodb_rs_members_optimeDate{member_state="PRIMARY"} - on (set) group_right mongodb_rs_members_optimeDate{member_state="SECONDARY"} > 10'
    ) == {
        "code": '(mongodb_rs_members_optimeDate{member_state="PRIMARY"} - on (set) '
        "group_right () "
        'mongodb_rs_members_optimeDate{member_state="SECONDARY"}) > 10',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'mongodb_rs_members_optimeDate{member_state="PRIMARY"} '
            "- on (set) group_right () "
            'mongodb_rs_members_optimeDate{member_state="SECONDARY"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_167():
    assert split_binary_op(
        'sum(avg(mongodb_oplog_stats_start - mongodb_oplog_stats_end)) - sum(avg(mongodb_rs_members_optimeDate{member_state="PRIMARY"} - on (set) group_right mongodb_rs_members_optimeDate{member_state="SECONDARY"})) <= 0'
    ) == {
        "code": "(sum(avg(mongodb_oplog_stats_start - mongodb_oplog_stats_end)) - "
        'sum(avg(mongodb_rs_members_optimeDate{member_state="PRIMARY"} - '
        "on (set) group_right () "
        'mongodb_rs_members_optimeDate{member_state="SECONDARY"}))) <= 0',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(avg(mongodb_oplog_stats_start - "
            "mongodb_oplog_stats_end)) - "
            'sum(avg(mongodb_rs_members_optimeDate{member_state="PRIMARY"} '
            "- on (set) group_right () "
            'mongodb_rs_members_optimeDate{member_state="SECONDARY"}))',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<=",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_168():
    assert split_binary_op(
        'mongodb_ss_metrics_cursor_open{csr_type="total"} > 10 * 1000'
    ) == {
        "code": 'mongodb_ss_metrics_cursor_open{csr_type="total"} > 10000',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'mongodb_ss_metrics_cursor_open{csr_type="total"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_169():
    assert split_binary_op(
        "increase(mongodb_ss_metrics_cursor_timedOut[1m]) > 100"
    ) == {
        "code": "increase(mongodb_ss_metrics_cursor_timedOut[1m]) > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(mongodb_ss_metrics_cursor_timedOut[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_170():
    assert split_binary_op(
        'avg by(instance) (rate(mongodb_ss_connections{conn_type="current"}[1m])) / avg by(instance) (sum (mongodb_ss_connections) by (instance)) * 100 > 80'
    ) == {
        "code": '((avg(rate(mongodb_ss_connections{conn_type="current"}[1m])) by '
        "(instance) / avg(sum(mongodb_ss_connections) by (instance)) by "
        "(instance)) * 100) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(avg(rate(mongodb_ss_connections{conn_type="current"}[1m])) '
            "by (instance) / avg(sum(mongodb_ss_connections) by "
            "(instance)) by (instance)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_171():
    assert split_binary_op(
        "(sum(mongodb_ss_mem_virtual) BY (instance) / sum(mongodb_ss_mem_resident) BY (instance)) > 3"
    ) == {
        "code": "(sum(mongodb_ss_mem_virtual) by (instance) / "
        "sum(mongodb_ss_mem_resident) by (instance)) > 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(mongodb_ss_mem_virtual) by (instance) / "
            "sum(mongodb_ss_mem_resident) by (instance)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_172():
    assert split_binary_op("zk_up == 0") == {
        "code": "zk_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "zk_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_173():
    assert split_binary_op("sum(zk_server_leader) == 0") == {
        "code": "sum(zk_server_leader) == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(zk_server_leader)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_174():
    assert split_binary_op("sum(zk_server_leader) > 1") == {
        "code": "sum(zk_server_leader) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(zk_server_leader)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_175():
    assert split_binary_op("zk_ruok == 0") == {
        "code": "zk_ruok == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "zk_ruok",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_176():
    assert split_binary_op(
        "increase(solr_metrics_core_update_handler_errors_total[1m]) > 1"
    ) == {
        "code": "increase(solr_metrics_core_update_handler_errors_total[1m]) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(solr_metrics_core_update_handler_errors_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_177():
    assert split_binary_op(
        'increase(solr_metrics_core_errors_total{category="QUERY"}[1m]) > 1'
    ) == {
        "code": 'increase(solr_metrics_core_errors_total{category="QUERY"}[1m]) > '
        "1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(solr_metrics_core_errors_total{category="QUERY"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_178():
    assert split_binary_op(
        'increase(solr_metrics_core_errors_total{category="REPLICATION"}[1m]) > 1'
    ) == {
        "code": 'increase(solr_metrics_core_errors_total{category="REPLICATION"}[1m]) '
        "> 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(solr_metrics_core_errors_total{category="REPLICATION"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_179():
    assert split_binary_op("solr_collections_live_nodes < 2") == {
        "code": "solr_collections_live_nodes < 2",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "solr_collections_live_nodes",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_180():
    assert split_binary_op('node_zfs_zpool_state{state!="online"} > 0') == {
        "code": 'node_zfs_zpool_state{state!="online"} > 0',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'node_zfs_zpool_state{state!="online"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_181():
    assert split_binary_op("nomad_nomad_job_summary_failed > 0") == {
        "code": "nomad_nomad_job_summary_failed > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "nomad_nomad_job_summary_failed",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_182():
    assert split_binary_op("nomad_nomad_job_summary_lost > 0") == {
        "code": "nomad_nomad_job_summary_lost > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "nomad_nomad_job_summary_lost",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_183():
    assert split_binary_op("nomad_nomad_job_summary_queued > 0") == {
        "code": "nomad_nomad_job_summary_queued > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "nomad_nomad_job_summary_queued",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_184():
    assert split_binary_op("nomad_nomad_blocked_evals_total_blocked > 0") == {
        "code": "nomad_nomad_blocked_evals_total_blocked > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "nomad_nomad_blocked_evals_total_blocked",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_185():
    assert split_binary_op("consul_catalog_service_node_healthy == 0") == {
        "code": "consul_catalog_service_node_healthy == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "consul_catalog_service_node_healthy",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_186():
    assert split_binary_op("consul_raft_peers < 3") == {
        "code": "consul_raft_peers < 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "consul_raft_peers",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_187():
    assert split_binary_op(
        'consul_health_node_status{status="critical"} == 1'
    ) == {
        "code": 'consul_health_node_status{status="critical"} == 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'consul_health_node_status{status="critical"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_188():
    assert split_binary_op("mssql_up == 0") == {
        "code": "mssql_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mssql_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_189():
    assert split_binary_op("increase(mssql_deadlocks[1m]) > 5") == {
        "code": "increase(mssql_deadlocks[1m]) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(mssql_deadlocks[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_190():
    assert split_binary_op(
        'sum(rate(nginx_http_requests_total{status=~"^4.."}[1m])) / sum(rate(nginx_http_requests_total[1m])) * 100 > 5'
    ) == {
        "code": '((sum(rate(nginx_http_requests_total{status=~"^4.."}[1m])) / '
        "sum(rate(nginx_http_requests_total[1m]))) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(nginx_http_requests_total{status=~"^4.."}[1m])) '
            "/ sum(rate(nginx_http_requests_total[1m]))) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_191():
    assert split_binary_op(
        'sum(rate(nginx_http_requests_total{status=~"^5.."}[1m])) / sum(rate(nginx_http_requests_total[1m])) * 100 > 5'
    ) == {
        "code": '((sum(rate(nginx_http_requests_total{status=~"^5.."}[1m])) / '
        "sum(rate(nginx_http_requests_total[1m]))) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(nginx_http_requests_total{status=~"^5.."}[1m])) '
            "/ sum(rate(nginx_http_requests_total[1m]))) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_192():
    assert split_binary_op(
        "histogram_quantile(0.99, sum(rate(nginx_http_request_duration_seconds_bucket[2m])) by (host, node)) > 3"
    ) == {
        "code": "histogram_quantile(0.99, "
        "sum(rate(nginx_http_request_duration_seconds_bucket[2m])) by "
        "(host, node)) > 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            "sum(rate(nginx_http_request_duration_seconds_bucket[2m])) "
            "by (host, node))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_193():
    assert split_binary_op(
        "delta(kafka_burrow_partition_current_offset[1m]) < 0"
    ) == {
        "code": "delta(kafka_burrow_partition_current_offset[1m]) < 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "delta(kafka_burrow_partition_current_offset[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_194():
    assert split_binary_op(
        "kafka_burrow_topic_partition_offset - on(partition, cluster, topic) group_right() kafka_burrow_partition_current_offset >= (kafka_burrow_topic_partition_offset offset 15m - on(partition, cluster, topic) group_right() kafka_burrow_partition_current_offset offset 15m) AND kafka_burrow_topic_partition_offset - on(partition, cluster, topic) group_right() kafka_burrow_partition_current_offset > 0"
    ) == {
        "code": "((kafka_burrow_topic_partition_offset - on (partition, cluster, "
        "topic) group_right () kafka_burrow_partition_current_offset) >= "
        "(kafka_burrow_topic_partition_offset offset 15m - on (partition, "
        "cluster, topic) group_right () "
        "kafka_burrow_partition_current_offset offset 15m)) and "
        "((kafka_burrow_topic_partition_offset - on (partition, cluster, "
        "topic) group_right () kafka_burrow_partition_current_offset) > 0)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(kafka_burrow_topic_partition_offset - on (partition, "
            "cluster, topic) group_right () "
            "kafka_burrow_partition_current_offset) >= "
            "(kafka_burrow_topic_partition_offset offset 15m - on "
            "(partition, cluster, topic) group_right () "
            "kafka_burrow_partition_current_offset offset 15m)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "kafka_burrow_topic_partition_offset - on "
                "(partition, cluster, topic) group_right "
                "() kafka_burrow_partition_current_offset",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">=",
            "right": {
                "code": "kafka_burrow_topic_partition_offset "
                "offset 15m - on (partition, cluster, "
                "topic) group_right () "
                "kafka_burrow_partition_current_offset "
                "offset 15m",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "(kafka_burrow_topic_partition_offset - on "
            "(partition, cluster, topic) group_right () "
            "kafka_burrow_partition_current_offset) > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "kafka_burrow_topic_partition_offset - on "
                "(partition, cluster, topic) group_right "
                "() kafka_burrow_partition_current_offset",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_195():
    assert split_binary_op(
        "sum(kafka_topic_partition_in_sync_replica) by (topic) < 3"
    ) == {
        "code": "sum(kafka_topic_partition_in_sync_replica) by (topic) < 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(kafka_topic_partition_in_sync_replica) by (topic)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_196():
    assert split_binary_op(
        "sum(kafka_consumergroup_lag) by (consumergroup) > 50"
    ) == {
        "code": "sum(kafka_consumergroup_lag) by (consumergroup) > 50",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(kafka_consumergroup_lag) by (consumergroup)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "50",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_197():
    assert split_binary_op(
        "sum(rate(request_errors_total[1m])) by (deployment, statefulset, daemonset) / sum(rate(request_total[1m])) by (deployment, statefulset, daemonset) * 100 > 10"
    ) == {
        "code": "((sum(rate(request_errors_total[1m])) by (deployment, "
        "statefulset, daemonset) / sum(rate(request_total[1m])) by "
        "(deployment, statefulset, daemonset)) * 100) > 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(sum(rate(request_errors_total[1m])) by (deployment, "
            "statefulset, daemonset) / "
            "sum(rate(request_total[1m])) by (deployment, "
            "statefulset, daemonset)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_198():
    assert split_binary_op(
        'changes(cassandra_stats{name="org:apache:cassandra:metrics:storage:totalhints:count"}[1m]) > 3'
    ) == {
        "code": 'changes(cassandra_stats{name="org:apache:cassandra:metrics:storage:totalhints:count"}[1m]) '
        "> 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'changes(cassandra_stats{name="org:apache:cassandra:metrics:storage:totalhints:count"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_199():
    assert split_binary_op(
        'avg_over_time(cassandra_stats{name="org:apache:cassandra:metrics:compaction:pendingtasks:value"}[1m]) > 100'
    ) == {
        "code": 'avg_over_time(cassandra_stats{name="org:apache:cassandra:metrics:compaction:pendingtasks:value"}[1m]) '
        "> 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'avg_over_time(cassandra_stats{name="org:apache:cassandra:metrics:compaction:pendingtasks:value"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_200():
    assert split_binary_op(
        'cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:viewwrite:viewwritelatency:99thpercentile",service="cas"} > 100000'
    ) == {
        "code": 'cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:viewwrite:viewwritelatency:99thpercentile", '
        'service="cas"} > 100000',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:viewwrite:viewwritelatency:99thpercentile", '
            'service="cas"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_201():
    assert split_binary_op(
        'rate(cassandra_stats{name="org:apache:cassandra:metrics:client:authfailure:count"}[1m]) > 5'
    ) == {
        "code": 'rate(cassandra_stats{name="org:apache:cassandra:metrics:client:authfailure:count"}[1m]) '
        "> 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rate(cassandra_stats{name="org:apache:cassandra:metrics:client:authfailure:count"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_202():
    assert split_binary_op(
        'sum(cassandra_stats{name="org:apache:cassandra:net:failuredetector:downendpointcount"}) by (service,group,cluster,env) > 0'
    ) == {
        "code": 'sum(cassandra_stats{name="org:apache:cassandra:net:failuredetector:downendpointcount"}) '
        "by (service, group, cluster, env) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(cassandra_stats{name="org:apache:cassandra:net:failuredetector:downendpointcount"}) '
            "by (service, group, cluster, env)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_203():
    assert split_binary_op(
        'cassandra_stats{name="org:apache:cassandra:metrics:commitlog:pendingtasks:value"} > 15'
    ) == {
        "code": 'cassandra_stats{name="org:apache:cassandra:metrics:commitlog:pendingtasks:value"} '
        "> 15",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_stats{name="org:apache:cassandra:metrics:commitlog:pendingtasks:value"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "15",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_204():
    assert split_binary_op(
        'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:compactionexecutor:currentlyblockedtasks:count"} > 0'
    ) == {
        "code": 'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:compactionexecutor:currentlyblockedtasks:count"} '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:compactionexecutor:currentlyblockedtasks:count"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_205():
    assert split_binary_op(
        'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:memtableflushwriter:currentlyblockedtasks:count"} > 0'
    ) == {
        "code": 'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:memtableflushwriter:currentlyblockedtasks:count"} '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:memtableflushwriter:currentlyblockedtasks:count"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_206():
    assert split_binary_op(
        'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:antientropystage:pendingtasks:value"} > 2'
    ) == {
        "code": 'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:antientropystage:pendingtasks:value"} '
        "> 2",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:antientropystage:pendingtasks:value"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_207():
    assert split_binary_op(
        'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:antientropystage:currentlyblockedtasks:count"} > 0'
    ) == {
        "code": 'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:antientropystage:currentlyblockedtasks:count"} '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_stats{name="org:apache:cassandra:metrics:threadpools:internal:antientropystage:currentlyblockedtasks:count"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_208():
    assert split_binary_op(
        'rate(cassandra_stats{name="org:apache:cassandra:metrics:connection:totaltimeouts:count"}[1m]) > 5'
    ) == {
        "code": 'rate(cassandra_stats{name="org:apache:cassandra:metrics:connection:totaltimeouts:count"}[1m]) '
        "> 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'rate(cassandra_stats{name="org:apache:cassandra:metrics:connection:totaltimeouts:count"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_209():
    assert split_binary_op(
        'changes(cassandra_stats{name="org:apache:cassandra:metrics:storage:exceptions:count"}[1m]) > 1'
    ) == {
        "code": 'changes(cassandra_stats{name="org:apache:cassandra:metrics:storage:exceptions:count"}[1m]) '
        "> 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'changes(cassandra_stats{name="org:apache:cassandra:metrics:storage:exceptions:count"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_210():
    assert split_binary_op(
        'cassandra_stats{name="org:apache:cassandra:metrics:table:tombstonescannedhistogram:99thpercentile"} > 1000'
    ) == {
        "code": 'cassandra_stats{name="org:apache:cassandra:metrics:table:tombstonescannedhistogram:99thpercentile"} '
        "> 1000",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_stats{name="org:apache:cassandra:metrics:table:tombstonescannedhistogram:99thpercentile"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_211():
    assert split_binary_op(
        'changes(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:write:unavailables:count"}[1m]) > 0'
    ) == {
        "code": 'changes(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:write:unavailables:count"}[1m]) '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'changes(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:write:unavailables:count"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_212():
    assert split_binary_op(
        'changes(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:read:unavailables:count"}[1m]) > 0'
    ) == {
        "code": 'changes(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:read:unavailables:count"}[1m]) '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'changes(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:read:unavailables:count"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_213():
    assert split_binary_op(
        'increase(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:write:failures:oneminuterate"}[1m]) > 0'
    ) == {
        "code": 'increase(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:write:failures:oneminuterate"}[1m]) '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:write:failures:oneminuterate"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_214():
    assert split_binary_op(
        'increase(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:read:failures:oneminuterate"}[1m]) > 0'
    ) == {
        "code": 'increase(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:read:failures:oneminuterate"}[1m]) '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(cassandra_stats{name="org:apache:cassandra:metrics:clientrequest:read:failures:oneminuterate"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_215():
    assert split_binary_op(
        'cassandra_stats{name="org:apache:cassandra:metrics:cache:keycache:hitrate:value"} < .85'
    ) == {
        "code": 'cassandra_stats{name="org:apache:cassandra:metrics:cache:keycache:hitrate:value"} '
        "< 0.85",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_stats{name="org:apache:cassandra:metrics:cache:keycache:hitrate:value"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "0.85",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_216():
    assert split_binary_op(
        "sum(cassandra_endpoint_active) by (cassandra_cluster,instance,exported_endpoint) < 1"
    ) == {
        "code": "sum(cassandra_endpoint_active) by (cassandra_cluster, instance, "
        "exported_endpoint) < 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(cassandra_endpoint_active) by (cassandra_cluster, "
            "instance, exported_endpoint)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_217():
    assert split_binary_op(
        "cassandra_table_estimated_pending_compactions > 100"
    ) == {
        "code": "cassandra_table_estimated_pending_compactions > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "cassandra_table_estimated_pending_compactions",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_218():
    assert split_binary_op("cassandra_commit_log_pending_tasks > 15") == {
        "code": "cassandra_commit_log_pending_tasks > 15",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "cassandra_commit_log_pending_tasks",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "15",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_219():
    assert split_binary_op(
        'cassandra_thread_pool_blocked_tasks{pool="CompactionExecutor"} > 15'
    ) == {
        "code": 'cassandra_thread_pool_blocked_tasks{pool="CompactionExecutor"} > '
        "15",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_thread_pool_blocked_tasks{pool="CompactionExecutor"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "15",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_220():
    assert split_binary_op(
        'cassandra_thread_pool_blocked_tasks{pool="MemtableFlushWriter"} > 15'
    ) == {
        "code": 'cassandra_thread_pool_blocked_tasks{pool="MemtableFlushWriter"} > '
        "15",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'cassandra_thread_pool_blocked_tasks{pool="MemtableFlushWriter"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "15",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_221():
    assert split_binary_op(
        "avg(cassandra_client_request_timeouts_total) by (cassandra_cluster,instance) > 5"
    ) == {
        "code": "avg(cassandra_client_request_timeouts_total) by "
        "(cassandra_cluster, instance) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "avg(cassandra_client_request_timeouts_total) by "
            "(cassandra_cluster, instance)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_222():
    assert split_binary_op(
        "changes(cassandra_storage_exceptions_total[1m]) > 1"
    ) == {
        "code": "changes(cassandra_storage_exceptions_total[1m]) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "changes(cassandra_storage_exceptions_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_223():
    assert split_binary_op(
        'avg(cassandra_table_tombstones_scanned{quantile="0.99"}) by (instance,cassandra_cluster,keyspace) > 100'
    ) == {
        "code": 'avg(cassandra_table_tombstones_scanned{quantile="0.99"}) by '
        "(instance, cassandra_cluster, keyspace) > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'avg(cassandra_table_tombstones_scanned{quantile="0.99"}) '
            "by (instance, cassandra_cluster, keyspace)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_224():
    assert split_binary_op(
        'changes(cassandra_client_request_unavailable_exceptions_total{operation="write"}[1m]) > 0'
    ) == {
        "code": 'changes(cassandra_client_request_unavailable_exceptions_total{operation="write"}[1m]) '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'changes(cassandra_client_request_unavailable_exceptions_total{operation="write"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_225():
    assert split_binary_op(
        'changes(cassandra_client_request_unavailable_exceptions_total{operation="read"}[1m]) > 0'
    ) == {
        "code": 'changes(cassandra_client_request_unavailable_exceptions_total{operation="read"}[1m]) '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'changes(cassandra_client_request_unavailable_exceptions_total{operation="read"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_226():
    assert split_binary_op(
        'increase(cassandra_client_request_failures_total{operation="write"}[1m]) > 0'
    ) == {
        "code": 'increase(cassandra_client_request_failures_total{operation="write"}[1m]) '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(cassandra_client_request_failures_total{operation="write"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_227():
    assert split_binary_op(
        'increase(cassandra_client_request_failures_total{operation="read"}[1m]) > 0'
    ) == {
        "code": 'increase(cassandra_client_request_failures_total{operation="read"}[1m]) '
        "> 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(cassandra_client_request_failures_total{operation="read"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_228():
    assert split_binary_op("mysql_up == 0") == {
        "code": "mysql_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mysql_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_229():
    assert split_binary_op(
        "max_over_time(mysql_global_status_threads_connected[1m]) / mysql_global_variables_max_connections * 100 > 80"
    ) == {
        "code": "((max_over_time(mysql_global_status_threads_connected[1m]) / "
        "mysql_global_variables_max_connections) * 100) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(max_over_time(mysql_global_status_threads_connected[1m]) "
            "/ mysql_global_variables_max_connections) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_230():
    assert split_binary_op(
        "max_over_time(mysql_global_status_threads_running[1m]) / mysql_global_variables_max_connections * 100 > 60"
    ) == {
        "code": "((max_over_time(mysql_global_status_threads_running[1m]) / "
        "mysql_global_variables_max_connections) * 100) > 60",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(max_over_time(mysql_global_status_threads_running[1m]) "
            "/ mysql_global_variables_max_connections) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "60",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_231():
    assert split_binary_op(
        "mysql_slave_status_master_server_id > 0 and ON (instance) mysql_slave_status_slave_io_running == 0"
    ) == {
        "code": "(mysql_slave_status_master_server_id > 0) and on (instance) "
        "(mysql_slave_status_slave_io_running == 0)",
        "group_modifier": {"args": ["instance"], "op": "on"},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mysql_slave_status_master_server_id > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "mysql_slave_status_master_server_id",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "mysql_slave_status_slave_io_running == 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "mysql_slave_status_slave_io_running",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_232():
    assert split_binary_op(
        "mysql_slave_status_master_server_id > 0 and ON (instance) mysql_slave_status_slave_sql_running == 0"
    ) == {
        "code": "(mysql_slave_status_master_server_id > 0) and on (instance) "
        "(mysql_slave_status_slave_sql_running == 0)",
        "group_modifier": {"args": ["instance"], "op": "on"},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mysql_slave_status_master_server_id > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "mysql_slave_status_master_server_id",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "mysql_slave_status_slave_sql_running == 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "mysql_slave_status_slave_sql_running",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_233():
    assert split_binary_op(
        "mysql_slave_status_master_server_id > 0 and ON (instance) (mysql_slave_status_seconds_behind_master - mysql_slave_status_sql_delay) > 30"
    ) == {
        "code": "(mysql_slave_status_master_server_id > 0) and on (instance) "
        "((mysql_slave_status_seconds_behind_master - "
        "mysql_slave_status_sql_delay) > 30)",
        "group_modifier": {"args": ["instance"], "op": "on"},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mysql_slave_status_master_server_id > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "mysql_slave_status_master_server_id",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "(mysql_slave_status_seconds_behind_master - "
            "mysql_slave_status_sql_delay) > 30",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "mysql_slave_status_seconds_behind_master "
                "- mysql_slave_status_sql_delay",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "30",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_234():
    assert split_binary_op(
        "increase(mysql_global_status_slow_queries[1m]) > 0"
    ) == {
        "code": "increase(mysql_global_status_slow_queries[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(mysql_global_status_slow_queries[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_235():
    assert split_binary_op(
        "rate(mysql_global_status_innodb_log_waits[15m]) > 10"
    ) == {
        "code": "rate(mysql_global_status_innodb_log_waits[15m]) > 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(mysql_global_status_innodb_log_waits[15m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_236():
    assert split_binary_op("mysql_global_status_uptime < 60") == {
        "code": "mysql_global_status_uptime < 60",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "mysql_global_status_uptime",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "60",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_237():
    assert split_binary_op("junos_up == 0") == {
        "code": "junos_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "junos_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_238():
    assert split_binary_op(
        "rate(junos_interface_transmit_bytes[1m]) * 8 > 1e+9 * 0.90"
    ) == {
        "code": "(rate(junos_interface_transmit_bytes[1m]) * 8) > 9e+08",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(junos_interface_transmit_bytes[1m]) * 8",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "9e+08",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_239():
    assert split_binary_op(
        "rate(junos_interface_transmit_bytes[1m]) * 8 > 1e+9 * 0.80"
    ) == {
        "code": "(rate(junos_interface_transmit_bytes[1m]) * 8) > 8e+08",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(junos_interface_transmit_bytes[1m]) * 8",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "8e+08",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_240():
    assert split_binary_op("count(etcd_server_id) % 2 == 0") == {
        "code": "(count(etcd_server_id) % 2) == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "count(etcd_server_id) % 2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_241():
    assert split_binary_op("etcd_server_has_leader == 0") == {
        "code": "etcd_server_has_leader == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "etcd_server_has_leader",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_242():
    assert split_binary_op(
        "increase(etcd_server_leader_changes_seen_total[10m]) > 2"
    ) == {
        "code": "increase(etcd_server_leader_changes_seen_total[10m]) > 2",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(etcd_server_leader_changes_seen_total[10m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_243():
    assert split_binary_op(
        'sum(rate(grpc_server_handled_total{grpc_code!="OK"}[1m])) BY (grpc_service, grpc_method) / sum(rate(grpc_server_handled_total[1m])) BY (grpc_service, grpc_method) > 0.01'
    ) == {
        "code": '(sum(rate(grpc_server_handled_total{grpc_code!="OK"}[1m])) by '
        "(grpc_service, grpc_method) / "
        "sum(rate(grpc_server_handled_total[1m])) by (grpc_service, "
        "grpc_method)) > 0.01",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(grpc_server_handled_total{grpc_code!="OK"}[1m])) '
            "by (grpc_service, grpc_method) / "
            "sum(rate(grpc_server_handled_total[1m])) by "
            "(grpc_service, grpc_method)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.01",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_244():
    assert split_binary_op(
        'sum(rate(grpc_server_handled_total{grpc_code!="OK"}[1m])) BY (grpc_service, grpc_method) / sum(rate(grpc_server_handled_total[1m])) BY (grpc_service, grpc_method) > 0.05'
    ) == {
        "code": '(sum(rate(grpc_server_handled_total{grpc_code!="OK"}[1m])) by '
        "(grpc_service, grpc_method) / "
        "sum(rate(grpc_server_handled_total[1m])) by (grpc_service, "
        "grpc_method)) > 0.05",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(grpc_server_handled_total{grpc_code!="OK"}[1m])) '
            "by (grpc_service, grpc_method) / "
            "sum(rate(grpc_server_handled_total[1m])) by "
            "(grpc_service, grpc_method)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.05",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_245():
    assert split_binary_op(
        'histogram_quantile(0.99, sum(rate(grpc_server_handling_seconds_bucket{grpc_type="unary"}[1m])) by (grpc_service, grpc_method, le)) > 0.15'
    ) == {
        "code": "histogram_quantile(0.99, "
        'sum(rate(grpc_server_handling_seconds_bucket{grpc_type="unary"}[1m])) '
        "by (grpc_service, grpc_method, le)) > 0.15",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            'sum(rate(grpc_server_handling_seconds_bucket{grpc_type="unary"}[1m])) '
            "by (grpc_service, grpc_method, le))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.15",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_246():
    assert split_binary_op(
        "sum(rate(etcd_http_failed_total[1m])) BY (method) / sum(rate(etcd_http_received_total[1m])) BY (method) > 0.01"
    ) == {
        "code": "(sum(rate(etcd_http_failed_total[1m])) by (method) / "
        "sum(rate(etcd_http_received_total[1m])) by (method)) > 0.01",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(etcd_http_failed_total[1m])) by (method) / "
            "sum(rate(etcd_http_received_total[1m])) by (method)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.01",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_247():
    assert split_binary_op(
        "sum(rate(etcd_http_failed_total[1m])) BY (method) / sum(rate(etcd_http_received_total[1m])) BY (method) > 0.05"
    ) == {
        "code": "(sum(rate(etcd_http_failed_total[1m])) by (method) / "
        "sum(rate(etcd_http_received_total[1m])) by (method)) > 0.05",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(etcd_http_failed_total[1m])) by (method) / "
            "sum(rate(etcd_http_received_total[1m])) by (method)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.05",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_248():
    assert split_binary_op(
        "histogram_quantile(0.99, rate(etcd_http_successful_duration_seconds_bucket[1m])) > 0.15"
    ) == {
        "code": "histogram_quantile(0.99, "
        "rate(etcd_http_successful_duration_seconds_bucket[1m])) > 0.15",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            "rate(etcd_http_successful_duration_seconds_bucket[1m]))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.15",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_249():
    assert split_binary_op(
        "histogram_quantile(0.99, rate(etcd_network_peer_round_trip_time_seconds_bucket[1m])) > 0.15"
    ) == {
        "code": "histogram_quantile(0.99, "
        "rate(etcd_network_peer_round_trip_time_seconds_bucket[1m])) > "
        "0.15",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            "rate(etcd_network_peer_round_trip_time_seconds_bucket[1m]))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.15",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_250():
    assert split_binary_op(
        "increase(etcd_server_proposals_failed_total[1h]) > 5"
    ) == {
        "code": "increase(etcd_server_proposals_failed_total[1h]) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(etcd_server_proposals_failed_total[1h])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_251():
    assert split_binary_op(
        "histogram_quantile(0.99, rate(etcd_disk_wal_fsync_duration_seconds_bucket[1m])) > 0.5"
    ) == {
        "code": "histogram_quantile(0.99, "
        "rate(etcd_disk_wal_fsync_duration_seconds_bucket[1m])) > 0.5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            "rate(etcd_disk_wal_fsync_duration_seconds_bucket[1m]))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_252():
    assert split_binary_op(
        "histogram_quantile(0.99, rate(etcd_disk_backend_commit_duration_seconds_bucket[1m])) > 0.25"
    ) == {
        "code": "histogram_quantile(0.99, "
        "rate(etcd_disk_backend_commit_duration_seconds_bucket[1m])) > "
        "0.25",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            "rate(etcd_disk_backend_commit_duration_seconds_bucket[1m]))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.25",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_253():
    assert split_binary_op("thanos_compact_halted == 1") == {
        "code": "thanos_compact_halted == 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "thanos_compact_halted",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_254():
    assert split_binary_op(
        "rate(thanos_objstore_bucket_operation_failures_total[1m]) > 0"
    ) == {
        "code": "rate(thanos_objstore_bucket_operation_failures_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(thanos_objstore_bucket_operation_failures_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_255():
    assert split_binary_op(
        "(time() - thanos_objstore_bucket_last_successful_upload_time) > 24*60*60"
    ) == {
        "code": "(time() - thanos_objstore_bucket_last_successful_upload_time) > "
        "86400",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "time() - "
            "thanos_objstore_bucket_last_successful_upload_time",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "86400",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_256():
    assert split_binary_op(
        "node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100 < 10"
    ) == {
        "code": "((node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * "
        "100) < 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(node_memory_MemAvailable_bytes / "
            "node_memory_MemTotal_bytes) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_257():
    assert split_binary_op("rate(node_vmstat_pgmajfault[1m]) > 1000") == {
        "code": "rate(node_vmstat_pgmajfault[1m]) > 1000",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(node_vmstat_pgmajfault[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_258():
    assert split_binary_op(
        "sum by (instance) (rate(node_network_receive_bytes_total[2m])) / 1024 / 1024 > 100"
    ) == {
        "code": "((sum(rate(node_network_receive_bytes_total[2m])) by (instance) / "
        "1024) / 1024) > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(sum(rate(node_network_receive_bytes_total[2m])) by "
            "(instance) / 1024) / 1024",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_259():
    assert split_binary_op(
        "sum by (instance) (rate(node_network_transmit_bytes_total[2m])) / 1024 / 1024 > 100"
    ) == {
        "code": "((sum(rate(node_network_transmit_bytes_total[2m])) by (instance) "
        "/ 1024) / 1024) > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(sum(rate(node_network_transmit_bytes_total[2m])) by "
            "(instance) / 1024) / 1024",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_260():
    assert split_binary_op(
        "sum by (instance) (rate(node_disk_read_bytes_total[2m])) / 1024 / 1024 > 50"
    ) == {
        "code": "((sum(rate(node_disk_read_bytes_total[2m])) by (instance) / 1024) "
        "/ 1024) > 50",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(sum(rate(node_disk_read_bytes_total[2m])) by "
            "(instance) / 1024) / 1024",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "50",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_261():
    assert split_binary_op(
        "sum by (instance) (rate(node_disk_written_bytes_total[2m])) / 1024 / 1024 > 50"
    ) == {
        "code": "((sum(rate(node_disk_written_bytes_total[2m])) by (instance) / "
        "1024) / 1024) > 50",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(sum(rate(node_disk_written_bytes_total[2m])) by "
            "(instance) / 1024) / 1024",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "50",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_262():
    assert split_binary_op(
        "(node_filesystem_avail_bytes * 100) / node_filesystem_size_bytes < 10 and ON (instance, device, mountpoint) node_filesystem_readonly == 0"
    ) == {
        "code": "(((node_filesystem_avail_bytes * 100) / "
        "node_filesystem_size_bytes) < 10) and on (instance, device, "
        "mountpoint) (node_filesystem_readonly == 0)",
        "group_modifier": {
            "args": ["instance", "device", "mountpoint"],
            "op": "on",
        },
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "((node_filesystem_avail_bytes * 100) / "
            "node_filesystem_size_bytes) < 10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "(node_filesystem_avail_bytes * 100) / "
                "node_filesystem_size_bytes",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "<",
            "right": {
                "code": "10",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "node_filesystem_readonly == 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "node_filesystem_readonly",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_263():
    assert split_binary_op(
        '(node_filesystem_avail_bytes * 100) / node_filesystem_size_bytes < 10 and ON (instance, device, mountpoint) predict_linear(node_filesystem_avail_bytes{fstype!~"tmpfs"}[1h], 24 * 3600) < 0 and ON (instance, device, mountpoint) node_filesystem_readonly == 0'
    ) == {
        "code": "((((node_filesystem_avail_bytes * 100) / "
        "node_filesystem_size_bytes) < 10) and on (instance, device, "
        "mountpoint) "
        '(predict_linear(node_filesystem_avail_bytes{fstype!~"tmpfs"}[1h], '
        "86400) < 0)) and on (instance, device, mountpoint) "
        "(node_filesystem_readonly == 0)",
        "group_modifier": {
            "args": ["instance", "device", "mountpoint"],
            "op": "on",
        },
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(((node_filesystem_avail_bytes * 100) / "
            "node_filesystem_size_bytes) < 10) and on (instance, "
            "device, mountpoint) "
            '(predict_linear(node_filesystem_avail_bytes{fstype!~"tmpfs"}[1h], '
            "86400) < 0)",
            "group_modifier": {
                "args": ["instance", "device", "mountpoint"],
                "op": "on",
            },
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "((node_filesystem_avail_bytes * 100) / "
                "node_filesystem_size_bytes) < 10",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": True,
                "join_modifier": {"args": None, "op": ""},
                "left": {
                    "code": "(node_filesystem_avail_bytes "
                    "* 100) / "
                    "node_filesystem_size_bytes",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": "<",
                "right": {
                    "code": "10",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
            "op": "and",
            "right": {
                "code": 'predict_linear(node_filesystem_avail_bytes{fstype!~"tmpfs"}[1h], '
                "86400) < 0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": True,
                "join_modifier": {"args": None, "op": ""},
                "left": {
                    "code": 'predict_linear(node_filesystem_avail_bytes{fstype!~"tmpfs"}[1h], '
                    "86400)",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": "<",
                "right": {
                    "code": "0",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
        },
        "op": "and",
        "right": {
            "code": "node_filesystem_readonly == 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "node_filesystem_readonly",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_264():
    assert split_binary_op(
        'node_filesystem_files_free{mountpoint ="/rootfs"} / node_filesystem_files{mountpoint="/rootfs"} * 100 < 10 and ON (instance, device, mountpoint) node_filesystem_readonly{mountpoint="/rootfs"} == 0'
    ) == {
        "code": '(((node_filesystem_files_free{mountpoint="/rootfs"} / '
        'node_filesystem_files{mountpoint="/rootfs"}) * 100) < 10) and on '
        "(instance, device, mountpoint) "
        '(node_filesystem_readonly{mountpoint="/rootfs"} == 0)',
        "group_modifier": {
            "args": ["instance", "device", "mountpoint"],
            "op": "on",
        },
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '((node_filesystem_files_free{mountpoint="/rootfs"} / '
            'node_filesystem_files{mountpoint="/rootfs"}) * 100) < '
            "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": '(node_filesystem_files_free{mountpoint="/rootfs"} '
                "/ "
                'node_filesystem_files{mountpoint="/rootfs"}) '
                "* 100",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "<",
            "right": {
                "code": "10",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": 'node_filesystem_readonly{mountpoint="/rootfs"} == 0',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": 'node_filesystem_readonly{mountpoint="/rootfs"}',
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_265():
    assert split_binary_op(
        'node_filesystem_files_free{mountpoint ="/rootfs"} / node_filesystem_files{mountpoint="/rootfs"} * 100 < 10 and predict_linear(node_filesystem_files_free{mountpoint="/rootfs"}[1h], 24 * 3600) < 0 and ON (instance, device, mountpoint) node_filesystem_readonly{mountpoint="/rootfs"} == 0'
    ) == {
        "code": '((((node_filesystem_files_free{mountpoint="/rootfs"} / '
        'node_filesystem_files{mountpoint="/rootfs"}) * 100) < 10) and '
        '(predict_linear(node_filesystem_files_free{mountpoint="/rootfs"}[1h], '
        "86400) < 0)) and on (instance, device, mountpoint) "
        '(node_filesystem_readonly{mountpoint="/rootfs"} == 0)',
        "group_modifier": {
            "args": ["instance", "device", "mountpoint"],
            "op": "on",
        },
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(((node_filesystem_files_free{mountpoint="/rootfs"} / '
            'node_filesystem_files{mountpoint="/rootfs"}) * 100) < '
            "10) and "
            '(predict_linear(node_filesystem_files_free{mountpoint="/rootfs"}[1h], '
            "86400) < 0)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": '((node_filesystem_files_free{mountpoint="/rootfs"} '
                "/ "
                'node_filesystem_files{mountpoint="/rootfs"}) '
                "* 100) < 10",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": True,
                "join_modifier": {"args": None, "op": ""},
                "left": {
                    "code": '(node_filesystem_files_free{mountpoint="/rootfs"} '
                    "/ "
                    'node_filesystem_files{mountpoint="/rootfs"}) '
                    "* 100",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": "<",
                "right": {
                    "code": "10",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
            "op": "and",
            "right": {
                "code": 'predict_linear(node_filesystem_files_free{mountpoint="/rootfs"}[1h], '
                "86400) < 0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": True,
                "join_modifier": {"args": None, "op": ""},
                "left": {
                    "code": 'predict_linear(node_filesystem_files_free{mountpoint="/rootfs"}[1h], '
                    "86400)",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": "<",
                "right": {
                    "code": "0",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
        },
        "op": "and",
        "right": {
            "code": 'node_filesystem_readonly{mountpoint="/rootfs"} == 0',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": 'node_filesystem_readonly{mountpoint="/rootfs"}',
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_266():
    assert split_binary_op(
        "rate(node_disk_read_time_seconds_total[1m]) / rate(node_disk_reads_completed_total[1m]) > 0.1 and rate(node_disk_reads_completed_total[1m]) > 0"
    ) == {
        "code": "((rate(node_disk_read_time_seconds_total[1m]) / "
        "rate(node_disk_reads_completed_total[1m])) > 0.1) and "
        "(rate(node_disk_reads_completed_total[1m]) > 0)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(rate(node_disk_read_time_seconds_total[1m]) / "
            "rate(node_disk_reads_completed_total[1m])) > 0.1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "rate(node_disk_read_time_seconds_total[1m]) "
                "/ "
                "rate(node_disk_reads_completed_total[1m])",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0.1",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "rate(node_disk_reads_completed_total[1m]) > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "rate(node_disk_reads_completed_total[1m])",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_267():
    assert split_binary_op(
        "rate(node_disk_write_time_seconds_total[1m]) / rate(node_disk_writes_completed_total[1m]) > 0.1 and rate(node_disk_writes_completed_total[1m]) > 0"
    ) == {
        "code": "((rate(node_disk_write_time_seconds_total[1m]) / "
        "rate(node_disk_writes_completed_total[1m])) > 0.1) and "
        "(rate(node_disk_writes_completed_total[1m]) > 0)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(rate(node_disk_write_time_seconds_total[1m]) / "
            "rate(node_disk_writes_completed_total[1m])) > 0.1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "rate(node_disk_write_time_seconds_total[1m]) "
                "/ "
                "rate(node_disk_writes_completed_total[1m])",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0.1",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "rate(node_disk_writes_completed_total[1m]) > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "rate(node_disk_writes_completed_total[1m])",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_268():
    assert split_binary_op(
        '100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[2m])) * 100) > 80'
    ) == {
        "code": '(100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[2m])) by '
        "(instance) * 100)) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "100 - "
            '(avg(rate(node_cpu_seconds_total{mode="idle"}[2m])) '
            "by (instance) * 100)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_269():
    assert split_binary_op(
        'avg by(instance) (rate(node_cpu_seconds_total{mode="steal"}[5m])) * 100 > 10'
    ) == {
        "code": '(avg(rate(node_cpu_seconds_total{mode="steal"}[5m])) by '
        "(instance) * 100) > 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'avg(rate(node_cpu_seconds_total{mode="steal"}[5m])) '
            "by (instance) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_270():
    assert split_binary_op(
        'avg by (instance) (rate(node_cpu_seconds_total{mode="iowait"}[5m])) * 100 > 5'
    ) == {
        "code": '(avg(rate(node_cpu_seconds_total{mode="iowait"}[5m])) by '
        "(instance) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'avg(rate(node_cpu_seconds_total{mode="iowait"}[5m])) '
            "by (instance) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_271():
    assert split_binary_op(
        '(rate(node_context_switches_total[5m])) / (count without(cpu, mode) (node_cpu_seconds_total{mode="idle"})) > 1000'
    ) == {
        "code": "(rate(node_context_switches_total[5m]) / "
        'count(node_cpu_seconds_total{mode="idle"}) without (cpu, mode)) > '
        "1000",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(node_context_switches_total[5m]) / "
            'count(node_cpu_seconds_total{mode="idle"}) without '
            "(cpu, mode)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_272():
    assert split_binary_op(
        "(1 - (node_memory_SwapFree_bytes / node_memory_SwapTotal_bytes)) * 100 > 80"
    ) == {
        "code": "((1 - (node_memory_SwapFree_bytes / node_memory_SwapTotal_bytes)) "
        "* 100) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(1 - (node_memory_SwapFree_bytes / "
            "node_memory_SwapTotal_bytes)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_273():
    assert split_binary_op('node_systemd_unit_state{state="failed"} == 1') == {
        "code": 'node_systemd_unit_state{state="failed"} == 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'node_systemd_unit_state{state="failed"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_274():
    assert split_binary_op("node_hwmon_temp_celsius > 75") == {
        "code": "node_hwmon_temp_celsius > 75",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "node_hwmon_temp_celsius",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "75",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_275():
    assert split_binary_op("node_hwmon_temp_crit_alarm_celsius == 1") == {
        "code": "node_hwmon_temp_crit_alarm_celsius == 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "node_hwmon_temp_crit_alarm_celsius",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_276():
    assert split_binary_op('node_md_state{state="inactive"} > 0') == {
        "code": 'node_md_state{state="inactive"} > 0',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'node_md_state{state="inactive"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_277():
    assert split_binary_op('node_md_disks{state="failed"} > 0') == {
        "code": 'node_md_disks{state="failed"} > 0',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'node_md_disks{state="failed"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_278():
    assert split_binary_op(
        'count(sum(label_replace(node_uname_info, "kernel", "$1", "release", "([0-9]+.[0-9]+.[0-9]+).*")) by (kernel)) > 1'
    ) == {
        "code": 'count(sum(label_replace(node_uname_info, "kernel", "$1", '
        '"release", "([0-9]+.[0-9]+.[0-9]+).*")) by (kernel)) > 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'count(sum(label_replace(node_uname_info, "kernel", '
            '"$1", "release", "([0-9]+.[0-9]+.[0-9]+).*")) by '
            "(kernel))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_279():
    assert split_binary_op("increase(node_vmstat_oom_kill[1m]) > 0") == {
        "code": "increase(node_vmstat_oom_kill[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(node_vmstat_oom_kill[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_280():
    assert split_binary_op(
        "increase(node_edac_correctable_errors_total[1m]) > 0"
    ) == {
        "code": "increase(node_edac_correctable_errors_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(node_edac_correctable_errors_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_281():
    assert split_binary_op("node_edac_uncorrectable_errors_total > 0") == {
        "code": "node_edac_uncorrectable_errors_total > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "node_edac_uncorrectable_errors_total",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_282():
    assert split_binary_op(
        "rate(node_network_receive_errs_total[2m]) / rate(node_network_receive_packets_total[2m]) > 0.01"
    ) == {
        "code": "(rate(node_network_receive_errs_total[2m]) / "
        "rate(node_network_receive_packets_total[2m])) > 0.01",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(node_network_receive_errs_total[2m]) / "
            "rate(node_network_receive_packets_total[2m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.01",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_283():
    assert split_binary_op(
        "rate(node_network_transmit_errs_total[2m]) / rate(node_network_transmit_packets_total[2m]) > 0.01"
    ) == {
        "code": "(rate(node_network_transmit_errs_total[2m]) / "
        "rate(node_network_transmit_packets_total[2m])) > 0.01",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(node_network_transmit_errs_total[2m]) / "
            "rate(node_network_transmit_packets_total[2m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.01",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_285():
    assert split_binary_op(
        "(node_bonding_active - node_bonding_slaves) != 0"
    ) == {
        "code": "(node_bonding_active - node_bonding_slaves) != 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "node_bonding_active - node_bonding_slaves",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_286():
    assert split_binary_op(
        "node_nf_conntrack_entries / node_nf_conntrack_entries_limit > 0.8"
    ) == {
        "code": "(node_nf_conntrack_entries / node_nf_conntrack_entries_limit) > "
        "0.8",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "node_nf_conntrack_entries / "
            "node_nf_conntrack_entries_limit",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0.8",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_287():
    assert split_binary_op(
        "(node_timex_offset_seconds > 0.05 and deriv(node_timex_offset_seconds[5m]) >= 0) or (node_timex_offset_seconds < -0.05 and deriv(node_timex_offset_seconds[5m]) <= 0)"
    ) == {
        "code": "((node_timex_offset_seconds > 0.05) and "
        "(deriv(node_timex_offset_seconds[5m]) >= 0)) or "
        "((node_timex_offset_seconds < -0.05) and "
        "(deriv(node_timex_offset_seconds[5m]) <= 0))",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(node_timex_offset_seconds > 0.05) and "
            "(deriv(node_timex_offset_seconds[5m]) >= 0)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "node_timex_offset_seconds > 0.05",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": True,
                "join_modifier": {"args": None, "op": ""},
                "left": {
                    "code": "node_timex_offset_seconds",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": ">",
                "right": {
                    "code": "0.05",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
            "op": "and",
            "right": {
                "code": "deriv(node_timex_offset_seconds[5m]) >= " "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": True,
                "join_modifier": {"args": None, "op": ""},
                "left": {
                    "code": "deriv(node_timex_offset_seconds[5m])",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": ">=",
                "right": {
                    "code": "0",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
        },
        "op": "or",
        "right": {
            "code": "(node_timex_offset_seconds < -0.05) and "
            "(deriv(node_timex_offset_seconds[5m]) <= 0)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "node_timex_offset_seconds < -0.05",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": True,
                "join_modifier": {"args": None, "op": ""},
                "left": {
                    "code": "node_timex_offset_seconds",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": "<",
                "right": {
                    "code": "-0.05",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
            "op": "and",
            "right": {
                "code": "deriv(node_timex_offset_seconds[5m]) <= " "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": True,
                "join_modifier": {"args": None, "op": ""},
                "left": {
                    "code": "deriv(node_timex_offset_seconds[5m])",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": "<=",
                "right": {
                    "code": "0",
                    "group_modifier": {"args": None, "op": ""},
                    "is_binary_op": False,
                    "join_modifier": {"args": None, "op": ""},
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
        },
    }


def test_case_288():
    assert split_binary_op(
        "min_over_time(node_timex_sync_status[1m]) == 0 and node_timex_maxerror_seconds >= 16"
    ) == {
        "code": "(min_over_time(node_timex_sync_status[1m]) == 0) and "
        "(node_timex_maxerror_seconds >= 16)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "min_over_time(node_timex_sync_status[1m]) == 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "min_over_time(node_timex_sync_status[1m])",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "node_timex_maxerror_seconds >= 16",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "node_timex_maxerror_seconds",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">=",
            "right": {
                "code": "16",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_289():
    assert split_binary_op("node_reboot_required > 0") == {
        "code": "node_reboot_required > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "node_reboot_required",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_290():
    assert split_binary_op(
        "sum(pulsar_subscription_back_log) by (subscription) > 5000"
    ) == {
        "code": "sum(pulsar_subscription_back_log) by (subscription) > 5000",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(pulsar_subscription_back_log) by (subscription)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_291():
    assert split_binary_op(
        "sum(pulsar_subscription_back_log) by (subscription) > 100000"
    ) == {
        "code": "sum(pulsar_subscription_back_log) by (subscription) > 100000",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(pulsar_subscription_back_log) by (subscription)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100000",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_292():
    assert split_binary_op(
        "sum(pulsar_storage_size > 5*1024*1024*1024) by (topic)"
    ) == {
        "code": "sum(pulsar_storage_size > 5.36870912e+09) by (topic)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_294():
    assert split_binary_op(
        "sum(pulsar_storage_write_latency_overflow > 0) by (topic)"
    ) == {
        "code": "sum(pulsar_storage_write_latency_overflow > 0) by (topic)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_295():
    assert split_binary_op(
        "sum(pulsar_entry_size_overflow > 0) by (topic)"
    ) == {
        "code": "sum(pulsar_entry_size_overflow > 0) by (topic)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_296():
    assert split_binary_op(
        "sum(bookie_ledger_dir__pulsar_data_bookkeeper_ledgers_usage) by (kubernetes_pod_name) > 75"
    ) == {
        "code": "sum(bookie_ledger_dir__pulsar_data_bookkeeper_ledgers_usage) by "
        "(kubernetes_pod_name) > 75",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(bookie_ledger_dir__pulsar_data_bookkeeper_ledgers_usage) "
            "by (kubernetes_pod_name)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "75",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_297():
    assert split_binary_op("count(bookie_SERVER_STATUS{} == 0) by (pod)") == {
        "code": "count(bookie_SERVER_STATUS == 0) by (pod)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_298():
    assert split_binary_op(
        "sum((rate(pulsar_function_user_exceptions_total{}[1m]) + rate(pulsar_function_system_exceptions_total{}[1m])) > 10) by (name)"
    ) == {
        "code": "sum((rate(pulsar_function_user_exceptions_total[1m]) + "
        "rate(pulsar_function_system_exceptions_total[1m])) > 10) by "
        "(name)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_299():
    assert split_binary_op(
        "sum(rate(pulsar_sink_sink_exceptions_total{}[1m]) > 10) by (name)"
    ) == {
        "code": "sum(rate(pulsar_sink_sink_exceptions_total[1m]) > 10) by (name)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_300():
    assert split_binary_op("jenkins_node_offline_value > 1") == {
        "code": "jenkins_node_offline_value > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "jenkins_node_offline_value",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_301():
    assert split_binary_op("jenkins_health_check_score < 1") == {
        "code": "jenkins_health_check_score < 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "jenkins_health_check_score",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_302():
    assert split_binary_op(
        "sum(jenkins_plugins_withUpdate) by (instance) > 3"
    ) == {
        "code": "sum(jenkins_plugins_withUpdate) by (instance) > 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(jenkins_plugins_withUpdate) by (instance)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_303():
    assert split_binary_op("default_jenkins_builds_health_score < 1") == {
        "code": "default_jenkins_builds_health_score < 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "default_jenkins_builds_health_score",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_304():
    assert split_binary_op("delta(jenkins_runs_failure_total[1h]) > 100") == {
        "code": "delta(jenkins_runs_failure_total[1h]) > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "delta(jenkins_runs_failure_total[1h])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_305():
    assert split_binary_op(
        "default_jenkins_builds_last_build_tests_failing > 0"
    ) == {
        "code": "default_jenkins_builds_last_build_tests_failing > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "default_jenkins_builds_last_build_tests_failing",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_306():
    assert split_binary_op(
        "default_jenkins_builds_last_build_result_ordinal == 2"
    ) == {
        "code": "default_jenkins_builds_last_build_result_ordinal == 2",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "default_jenkins_builds_last_build_result_ordinal",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "2",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_307():
    assert split_binary_op(
        "pgbouncer_pools_server_active_connections > 200"
    ) == {
        "code": "pgbouncer_pools_server_active_connections > 200",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "pgbouncer_pools_server_active_connections",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "200",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_308():
    assert split_binary_op(
        'increase(pgbouncer_errors_count{errmsg!="server conn crashed?"}[1m]) > 10'
    ) == {
        "code": 'increase(pgbouncer_errors_count{errmsg!="server conn '
        'crashed?"}[1m]) > 10',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(pgbouncer_errors_count{errmsg!="server conn '
            'crashed?"}[1m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_309():
    assert split_binary_op(
        'increase(pgbouncer_errors_count{errmsg="no more connections allowed (max_client_conn)"}[30s]) > 0'
    ) == {
        "code": 'increase(pgbouncer_errors_count{errmsg="no more connections '
        'allowed (max_client_conn)"}[30s]) > 0',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(pgbouncer_errors_count{errmsg="no more '
            'connections allowed (max_client_conn)"}[30s])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_310():
    assert split_binary_op(
        'kube_node_status_condition{condition="Ready",status="true"} == 0'
    ) == {
        "code": 'kube_node_status_condition{condition="Ready", status="true"} == 0',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'kube_node_status_condition{condition="Ready", '
            'status="true"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_311():
    assert split_binary_op(
        'kube_node_status_condition{condition="MemoryPressure",status="true"} == 1'
    ) == {
        "code": 'kube_node_status_condition{condition="MemoryPressure", '
        'status="true"} == 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'kube_node_status_condition{condition="MemoryPressure", '
            'status="true"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_312():
    assert split_binary_op(
        'kube_node_status_condition{condition="DiskPressure",status="true"} == 1'
    ) == {
        "code": 'kube_node_status_condition{condition="DiskPressure", '
        'status="true"} == 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'kube_node_status_condition{condition="DiskPressure", '
            'status="true"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_313():
    assert split_binary_op(
        'kube_node_status_condition{condition="OutOfDisk",status="true"} == 1'
    ) == {
        "code": 'kube_node_status_condition{condition="OutOfDisk", status="true"} '
        "== 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'kube_node_status_condition{condition="OutOfDisk", '
            'status="true"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_314():
    assert split_binary_op(
        'sum by (node) ((kube_pod_status_phase{phase="Running"} == 1) + on(uid) group_left(node) (0 * kube_pod_info{pod_template_hash=""})) / sum by (node) (kube_node_status_allocatable{resource="pods"}) * 100 > 90'
    ) == {
        "code": '((sum((kube_pod_status_phase{phase="Running"} == 1) + on (uid) '
        'group_left (node) (0 * kube_pod_info{pod_template_hash=""})) by '
        '(node) / sum(kube_node_status_allocatable{resource="pods"}) by '
        "(node)) * 100) > 90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum((kube_pod_status_phase{phase="Running"} == 1) + '
            "on (uid) group_left (node) (0 * "
            'kube_pod_info{pod_template_hash=""})) by (node) / '
            'sum(kube_node_status_allocatable{resource="pods"}) by '
            "(node)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_315():
    assert split_binary_op(
        '(kube_pod_container_status_restarts_total - kube_pod_container_status_restarts_total offset 10m >= 1) and ignoring (reason) min_over_time(kube_pod_container_status_last_terminated_reason{reason="OOMKilled"}[10m]) == 1'
    ) == {
        "code": "((kube_pod_container_status_restarts_total - "
        "kube_pod_container_status_restarts_total offset 10m) >= 1) and "
        "ignoring (reason) "
        '(min_over_time(kube_pod_container_status_last_terminated_reason{reason="OOMKilled"}[10m]) '
        "== 1)",
        "group_modifier": {"args": ["reason"], "op": "ignoring"},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(kube_pod_container_status_restarts_total - "
            "kube_pod_container_status_restarts_total offset 10m) "
            ">= 1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "kube_pod_container_status_restarts_total "
                "- "
                "kube_pod_container_status_restarts_total "
                "offset 10m",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">=",
            "right": {
                "code": "1",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": 'min_over_time(kube_pod_container_status_last_terminated_reason{reason="OOMKilled"}[10m]) '
            "== 1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": 'min_over_time(kube_pod_container_status_last_terminated_reason{reason="OOMKilled"}[10m])',
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "1",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_316():
    assert split_binary_op("kube_job_status_failed > 0") == {
        "code": "kube_job_status_failed > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_job_status_failed",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_317():
    assert split_binary_op("kube_cronjob_spec_suspend != 0") == {
        "code": "kube_cronjob_spec_suspend != 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_cronjob_spec_suspend",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_318():
    assert split_binary_op(
        'kube_persistentvolumeclaim_status_phase{phase="Pending"} == 1'
    ) == {
        "code": 'kube_persistentvolumeclaim_status_phase{phase="Pending"} == 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'kube_persistentvolumeclaim_status_phase{phase="Pending"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_319():
    assert split_binary_op(
        "kubelet_volume_stats_available_bytes / kubelet_volume_stats_capacity_bytes * 100 < 10"
    ) == {
        "code": "((kubelet_volume_stats_available_bytes / "
        "kubelet_volume_stats_capacity_bytes) * 100) < 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(kubelet_volume_stats_available_bytes / "
            "kubelet_volume_stats_capacity_bytes) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_320():
    assert split_binary_op(
        "predict_linear(kubelet_volume_stats_available_bytes[6h], 4 * 24 * 3600) < 0"
    ) == {
        "code": "predict_linear(kubelet_volume_stats_available_bytes[6h], 345600) "
        "< 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "predict_linear(kubelet_volume_stats_available_bytes[6h], "
            "345600)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_321():
    assert split_binary_op(
        'kube_persistentvolume_status_phase{phase=~"Failed|Pending", job="kube-state-metrics"} > 0'
    ) == {
        "code": 'kube_persistentvolume_status_phase{phase=~"Failed|Pending", '
        'job="kube-state-metrics"} > 0',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'kube_persistentvolume_status_phase{phase=~"Failed|Pending", '
            'job="kube-state-metrics"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_322():
    assert split_binary_op(
        "(kube_statefulset_status_replicas_ready / kube_statefulset_status_replicas_current) != 1"
    ) == {
        "code": "(kube_statefulset_status_replicas_ready / "
        "kube_statefulset_status_replicas_current) != 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_statefulset_status_replicas_ready / "
            "kube_statefulset_status_replicas_current",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_323():
    assert split_binary_op(
        'kube_horizontalpodautoscaler_status_condition{status="false", condition="AbleToScale"} == 1'
    ) == {
        "code": 'kube_horizontalpodautoscaler_status_condition{status="false", '
        'condition="AbleToScale"} == 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'kube_horizontalpodautoscaler_status_condition{status="false", '
            'condition="AbleToScale"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_324():
    assert split_binary_op(
        'kube_horizontalpodautoscaler_status_condition{status="false", condition="ScalingActive"} == 1'
    ) == {
        "code": 'kube_horizontalpodautoscaler_status_condition{status="false", '
        'condition="ScalingActive"} == 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'kube_horizontalpodautoscaler_status_condition{status="false", '
            'condition="ScalingActive"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_325():
    assert split_binary_op(
        "kube_horizontalpodautoscaler_status_desired_replicas >= kube_horizontalpodautoscaler_spec_max_replicas"
    ) == {
        "code": "kube_horizontalpodautoscaler_status_desired_replicas >= "
        "kube_horizontalpodautoscaler_spec_max_replicas",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_horizontalpodautoscaler_status_desired_replicas",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">=",
        "right": {
            "code": "kube_horizontalpodautoscaler_spec_max_replicas",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_326():
    assert split_binary_op(
        'min_over_time(sum by (namespace, pod) (kube_pod_status_phase{phase=~"Pending|Unknown|Failed"})[15m:1m]) > 0'
    ) == {
        "code": 'min_over_time((sum(kube_pod_status_phase{phase=~"Pending|Unknown|Failed"}) '
        "by (namespace, pod))[15m:1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'min_over_time((sum(kube_pod_status_phase{phase=~"Pending|Unknown|Failed"}) '
            "by (namespace, pod))[15m:1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_327():
    assert split_binary_op(
        "increase(kube_pod_container_status_restarts_total[1m]) > 3"
    ) == {
        "code": "increase(kube_pod_container_status_restarts_total[1m]) > 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(kube_pod_container_status_restarts_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_328():
    assert split_binary_op(
        "kube_replicaset_spec_replicas != kube_replicaset_status_ready_replicas"
    ) == {
        "code": "kube_replicaset_spec_replicas != "
        "kube_replicaset_status_ready_replicas",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_replicaset_spec_replicas",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "kube_replicaset_status_ready_replicas",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_329():
    assert split_binary_op(
        "kube_deployment_spec_replicas != kube_deployment_status_replicas_available"
    ) == {
        "code": "kube_deployment_spec_replicas != "
        "kube_deployment_status_replicas_available",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_deployment_spec_replicas",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "kube_deployment_status_replicas_available",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_330():
    assert split_binary_op(
        "kube_statefulset_status_replicas_ready != kube_statefulset_status_replicas"
    ) == {
        "code": "kube_statefulset_status_replicas_ready != "
        "kube_statefulset_status_replicas",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_statefulset_status_replicas_ready",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "kube_statefulset_status_replicas",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_331():
    assert split_binary_op(
        "kube_deployment_status_observed_generation != kube_deployment_metadata_generation"
    ) == {
        "code": "kube_deployment_status_observed_generation != "
        "kube_deployment_metadata_generation",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_deployment_status_observed_generation",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "kube_deployment_metadata_generation",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_332():
    assert split_binary_op(
        "kube_statefulset_status_observed_generation != kube_statefulset_metadata_generation"
    ) == {
        "code": "kube_statefulset_status_observed_generation != "
        "kube_statefulset_metadata_generation",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_statefulset_status_observed_generation",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "kube_statefulset_metadata_generation",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_333():
    assert split_binary_op(
        "max without (revision) (kube_statefulset_status_current_revision unless kube_statefulset_status_update_revision) * (kube_statefulset_replicas != kube_statefulset_status_replicas_updated)"
    ) == {
        "code": "max(kube_statefulset_status_current_revision unless "
        "kube_statefulset_status_update_revision) without (revision) * "
        "(kube_statefulset_replicas != "
        "kube_statefulset_status_replicas_updated)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_334():
    assert split_binary_op(
        "kube_daemonset_status_number_ready / kube_daemonset_status_desired_number_scheduled * 100 < 100 or kube_daemonset_status_desired_number_scheduled - kube_daemonset_status_current_number_scheduled > 0"
    ) == {
        "code": "(((kube_daemonset_status_number_ready / "
        "kube_daemonset_status_desired_number_scheduled) * 100) < 100) or "
        "((kube_daemonset_status_desired_number_scheduled - "
        "kube_daemonset_status_current_number_scheduled) > 0)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "((kube_daemonset_status_number_ready / "
            "kube_daemonset_status_desired_number_scheduled) * "
            "100) < 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "(kube_daemonset_status_number_ready / "
                "kube_daemonset_status_desired_number_scheduled) "
                "* 100",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "<",
            "right": {
                "code": "100",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "or",
        "right": {
            "code": "(kube_daemonset_status_desired_number_scheduled - "
            "kube_daemonset_status_current_number_scheduled) > 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "kube_daemonset_status_desired_number_scheduled "
                "- "
                "kube_daemonset_status_current_number_scheduled",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_335():
    assert split_binary_op(
        "kube_daemonset_status_number_misscheduled > 0"
    ) == {
        "code": "kube_daemonset_status_number_misscheduled > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_daemonset_status_number_misscheduled",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_336():
    assert split_binary_op(
        "time() - kube_cronjob_next_schedule_time > 3600"
    ) == {
        "code": "(time() - kube_cronjob_next_schedule_time) > 3600",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "time() - kube_cronjob_next_schedule_time",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3600",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_337():
    assert split_binary_op(
        "kube_job_spec_completions - kube_job_status_succeeded > 0"
    ) == {
        "code": "(kube_job_spec_completions - kube_job_status_succeeded) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "kube_job_spec_completions - kube_job_status_succeeded",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_338():
    assert split_binary_op(
        'sum(rate(apiserver_request_total{job="apiserver",code=~"^(?:5..)$"}[1m])) / sum(rate(apiserver_request_total{job="apiserver"}[1m])) * 100 > 3'
    ) == {
        "code": '((sum(rate(apiserver_request_total{job="apiserver", '
        'code=~"^(?:5..)$"}[1m])) / '
        'sum(rate(apiserver_request_total{job="apiserver"}[1m]))) * 100) > '
        "3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(apiserver_request_total{job="apiserver", '
            'code=~"^(?:5..)$"}[1m])) / '
            'sum(rate(apiserver_request_total{job="apiserver"}[1m]))) '
            "* 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_339():
    assert split_binary_op(
        '(sum(rate(rest_client_requests_total{code=~"(4|5).."}[1m])) by (instance, job) / sum(rate(rest_client_requests_total[1m])) by (instance, job)) * 100 > 1'
    ) == {
        "code": '((sum(rate(rest_client_requests_total{code=~"(4|5).."}[1m])) by '
        "(instance, job) / sum(rate(rest_client_requests_total[1m])) by "
        "(instance, job)) * 100) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(rest_client_requests_total{code=~"(4|5).."}[1m])) '
            "by (instance, job) / "
            "sum(rate(rest_client_requests_total[1m])) by "
            "(instance, job)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_340():
    assert split_binary_op(
        'apiserver_client_certificate_expiration_seconds_count{job="apiserver"} > 0 and histogram_quantile(0.01, sum by (job, le) (rate(apiserver_client_certificate_expiration_seconds_bucket{job="apiserver"}[5m]))) < 7*24*60*60'
    ) == {
        "code": '(apiserver_client_certificate_expiration_seconds_count{job="apiserver"} '
        "> 0) and (histogram_quantile(0.01, "
        'sum(rate(apiserver_client_certificate_expiration_seconds_bucket{job="apiserver"}[5m])) '
        "by (job, le)) < 604800)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'apiserver_client_certificate_expiration_seconds_count{job="apiserver"} '
            "> 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": 'apiserver_client_certificate_expiration_seconds_count{job="apiserver"}',
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "histogram_quantile(0.01, "
            'sum(rate(apiserver_client_certificate_expiration_seconds_bucket{job="apiserver"}[5m])) '
            "by (job, le)) < 604800",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "histogram_quantile(0.01, "
                'sum(rate(apiserver_client_certificate_expiration_seconds_bucket{job="apiserver"}[5m])) '
                "by (job, le))",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "<",
            "right": {
                "code": "604800",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_341():
    assert split_binary_op(
        'apiserver_client_certificate_expiration_seconds_count{job="apiserver"} > 0 and histogram_quantile(0.01, sum by (job, le) (rate(apiserver_client_certificate_expiration_seconds_bucket{job="apiserver"}[5m]))) < 24*60*60'
    ) == {
        "code": '(apiserver_client_certificate_expiration_seconds_count{job="apiserver"} '
        "> 0) and (histogram_quantile(0.01, "
        'sum(rate(apiserver_client_certificate_expiration_seconds_bucket{job="apiserver"}[5m])) '
        "by (job, le)) < 86400)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'apiserver_client_certificate_expiration_seconds_count{job="apiserver"} '
            "> 0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": 'apiserver_client_certificate_expiration_seconds_count{job="apiserver"}',
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "histogram_quantile(0.01, "
            'sum(rate(apiserver_client_certificate_expiration_seconds_bucket{job="apiserver"}[5m])) '
            "by (job, le)) < 86400",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "histogram_quantile(0.01, "
                'sum(rate(apiserver_client_certificate_expiration_seconds_bucket{job="apiserver"}[5m])) '
                "by (job, le))",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "<",
            "right": {
                "code": "86400",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_342():
    assert split_binary_op(
        'histogram_quantile(0.99, sum(rate(apiserver_request_latencies_bucket{subresource!="log",verb!~"^(?:CONNECT|WATCHLIST|WATCH|PROXY)$"} [10m])) WITHOUT (instance, resource)) / 1e+06 > 1'
    ) == {
        "code": "(histogram_quantile(0.99, "
        'sum(rate(apiserver_request_latencies_bucket{subresource!="log", '
        'verb!~"^(?:CONNECT|WATCHLIST|WATCH|PROXY)$"}[10m])) without '
        "(instance, resource)) / 1e+06) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "histogram_quantile(0.99, "
            'sum(rate(apiserver_request_latencies_bucket{subresource!="log", '
            'verb!~"^(?:CONNECT|WATCHLIST|WATCH|PROXY)$"}[10m])) '
            "without (instance, resource)) / 1e+06",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_343():
    assert split_binary_op("increase(coredns_panics_total[1m]) > 0") == {
        "code": "increase(coredns_panics_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(coredns_panics_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_344():
    assert split_binary_op("time() - container_last_seen > 60") == {
        "code": "(time() - container_last_seen) > 60",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "time() - container_last_seen",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "60",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_345():
    assert split_binary_op("absent(container_last_seen)") == {
        "code": "absent(container_last_seen)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": False,
        "join_modifier": {"args": None, "op": ""},
        "left": None,
        "op": "",
        "right": None,
    }


def test_case_346():
    assert split_binary_op(
        '(sum(rate(container_cpu_usage_seconds_total{name!=""}[3m])) BY (instance, name) * 100) > 80'
    ) == {
        "code": '(sum(rate(container_cpu_usage_seconds_total{name!=""}[3m])) by '
        "(instance, name) * 100) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(container_cpu_usage_seconds_total{name!=""}[3m])) '
            "by (instance, name) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_347():
    assert split_binary_op(
        '(sum(container_memory_working_set_bytes{name!=""}) BY (instance, name) / sum(container_spec_memory_limit_bytes > 0) BY (instance, name) * 100) > 80'
    ) == {
        "code": '((sum(container_memory_working_set_bytes{name!=""}) by (instance, '
        "name) / sum(container_spec_memory_limit_bytes > 0) by (instance, "
        "name)) * 100) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(container_memory_working_set_bytes{name!=""}) by '
            "(instance, name) / "
            "sum(container_spec_memory_limit_bytes > 0) by "
            "(instance, name)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_348():
    assert split_binary_op(
        '(1 - (sum(container_fs_inodes_free{name!=""}) BY (instance) / sum(container_fs_inodes_total) BY (instance))) * 100 > 80'
    ) == {
        "code": '((1 - (sum(container_fs_inodes_free{name!=""}) by (instance) / '
        "sum(container_fs_inodes_total) by (instance))) * 100) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(1 - (sum(container_fs_inodes_free{name!=""}) by '
            "(instance) / sum(container_fs_inodes_total) by "
            "(instance))) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_349():
    assert split_binary_op(
        "rate(container_cpu_cfs_throttled_seconds_total[3m]) > 1"
    ) == {
        "code": "rate(container_cpu_cfs_throttled_seconds_total[3m]) > 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "rate(container_cpu_cfs_throttled_seconds_total[3m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_350():
    assert split_binary_op("windows_exporter_collector_success == 0") == {
        "code": "windows_exporter_collector_success == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "windows_exporter_collector_success",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_351():
    assert split_binary_op('windows_service_status{status="ok"} != 1') == {
        "code": 'windows_service_status{status="ok"} != 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'windows_service_status{status="ok"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "!=",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_352():
    assert split_binary_op(
        '100 - (avg by (instance) (rate(windows_cpu_time_total{mode="idle"}[2m])) * 100) > 80'
    ) == {
        "code": '(100 - (avg(rate(windows_cpu_time_total{mode="idle"}[2m])) by '
        "(instance) * 100)) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "100 - "
            '(avg(rate(windows_cpu_time_total{mode="idle"}[2m])) '
            "by (instance) * 100)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_353():
    assert split_binary_op(
        "100 - ((windows_os_physical_memory_free_bytes / windows_cs_physical_memory_bytes) * 100) > 90"
    ) == {
        "code": "(100 - ((windows_os_physical_memory_free_bytes / "
        "windows_cs_physical_memory_bytes) * 100)) > 90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "100 - ((windows_os_physical_memory_free_bytes / "
            "windows_cs_physical_memory_bytes) * 100)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_354():
    assert split_binary_op(
        "100.0 - 100 * ((windows_logical_disk_free_bytes / 1024 / 1024 ) / (windows_logical_disk_size_bytes / 1024 / 1024)) > 80"
    ) == {
        "code": "(100 - (100 * (((windows_logical_disk_free_bytes / 1024) / 1024) "
        "/ ((windows_logical_disk_size_bytes / 1024) / 1024)))) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "100 - (100 * (((windows_logical_disk_free_bytes / "
            "1024) / 1024) / ((windows_logical_disk_size_bytes / "
            "1024) / 1024)))",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_355():
    assert split_binary_op(
        '(elasticsearch_jvm_memory_used_bytes{area="heap"} / elasticsearch_jvm_memory_max_bytes{area="heap"}) * 100 > 90'
    ) == {
        "code": '((elasticsearch_jvm_memory_used_bytes{area="heap"} / '
        'elasticsearch_jvm_memory_max_bytes{area="heap"}) * 100) > 90',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(elasticsearch_jvm_memory_used_bytes{area="heap"} / '
            'elasticsearch_jvm_memory_max_bytes{area="heap"}) * '
            "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_356():
    assert split_binary_op(
        '(elasticsearch_jvm_memory_used_bytes{area="heap"} / elasticsearch_jvm_memory_max_bytes{area="heap"}) * 100 > 80'
    ) == {
        "code": '((elasticsearch_jvm_memory_used_bytes{area="heap"} / '
        'elasticsearch_jvm_memory_max_bytes{area="heap"}) * 100) > 80',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(elasticsearch_jvm_memory_used_bytes{area="heap"} / '
            'elasticsearch_jvm_memory_max_bytes{area="heap"}) * '
            "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_357():
    assert split_binary_op(
        "elasticsearch_filesystem_data_available_bytes / elasticsearch_filesystem_data_size_bytes * 100 < 10"
    ) == {
        "code": "((elasticsearch_filesystem_data_available_bytes / "
        "elasticsearch_filesystem_data_size_bytes) * 100) < 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(elasticsearch_filesystem_data_available_bytes / "
            "elasticsearch_filesystem_data_size_bytes) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_358():
    assert split_binary_op(
        "elasticsearch_filesystem_data_available_bytes / elasticsearch_filesystem_data_size_bytes * 100 < 20"
    ) == {
        "code": "((elasticsearch_filesystem_data_available_bytes / "
        "elasticsearch_filesystem_data_size_bytes) * 100) < 20",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(elasticsearch_filesystem_data_available_bytes / "
            "elasticsearch_filesystem_data_size_bytes) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "20",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_359():
    assert split_binary_op(
        'elasticsearch_cluster_health_status{color="red"} == 1'
    ) == {
        "code": 'elasticsearch_cluster_health_status{color="red"} == 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'elasticsearch_cluster_health_status{color="red"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_360():
    assert split_binary_op(
        'elasticsearch_cluster_health_status{color="yellow"} == 1'
    ) == {
        "code": 'elasticsearch_cluster_health_status{color="yellow"} == 1',
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'elasticsearch_cluster_health_status{color="yellow"}',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_361():
    assert split_binary_op(
        "elasticsearch_cluster_health_number_of_nodes < 3"
    ) == {
        "code": "elasticsearch_cluster_health_number_of_nodes < 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "elasticsearch_cluster_health_number_of_nodes",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_362():
    assert split_binary_op(
        "elasticsearch_cluster_health_number_of_data_nodes < 3"
    ) == {
        "code": "elasticsearch_cluster_health_number_of_data_nodes < 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "elasticsearch_cluster_health_number_of_data_nodes",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_363():
    assert split_binary_op(
        "elasticsearch_cluster_health_relocating_shards > 0"
    ) == {
        "code": "elasticsearch_cluster_health_relocating_shards > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "elasticsearch_cluster_health_relocating_shards",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_364():
    assert split_binary_op(
        "elasticsearch_cluster_health_relocating_shards > 0"
    ) == {
        "code": "elasticsearch_cluster_health_relocating_shards > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "elasticsearch_cluster_health_relocating_shards",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_365():
    assert split_binary_op(
        "elasticsearch_cluster_health_initializing_shards > 0"
    ) == {
        "code": "elasticsearch_cluster_health_initializing_shards > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "elasticsearch_cluster_health_initializing_shards",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_366():
    assert split_binary_op(
        "elasticsearch_cluster_health_initializing_shards > 0"
    ) == {
        "code": "elasticsearch_cluster_health_initializing_shards > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "elasticsearch_cluster_health_initializing_shards",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_367():
    assert split_binary_op(
        "elasticsearch_cluster_health_unassigned_shards > 0"
    ) == {
        "code": "elasticsearch_cluster_health_unassigned_shards > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "elasticsearch_cluster_health_unassigned_shards",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_368():
    assert split_binary_op(
        "elasticsearch_cluster_health_number_of_pending_tasks > 0"
    ) == {
        "code": "elasticsearch_cluster_health_number_of_pending_tasks > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "elasticsearch_cluster_health_number_of_pending_tasks",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_369():
    assert split_binary_op(
        'increase(elasticsearch_indices_docs{es_data_node="true"}[10m]) < 1'
    ) == {
        "code": 'increase(elasticsearch_indices_docs{es_data_node="true"}[10m]) < '
        "1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'increase(elasticsearch_indices_docs{es_data_node="true"}[10m])',
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_370():
    assert split_binary_op("apache_up == 0") == {
        "code": "apache_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "apache_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_371():
    assert split_binary_op(
        '(sum by (instance) (apache_workers{state="busy"}) / sum by (instance) (apache_scoreboard) ) * 100 > 80'
    ) == {
        "code": '((sum(apache_workers{state="busy"}) by (instance) / '
        "sum(apache_scoreboard) by (instance)) * 100) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(apache_workers{state="busy"}) by (instance) / '
            "sum(apache_scoreboard) by (instance)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_372():
    assert split_binary_op("apache_uptime_seconds_total / 60 < 1") == {
        "code": "(apache_uptime_seconds_total / 60) < 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "apache_uptime_seconds_total / 60",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_373():
    assert split_binary_op(
        "count(traefik_backend_server_up) by (backend) == 0"
    ) == {
        "code": "count(traefik_backend_server_up) by (backend) == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "count(traefik_backend_server_up) by (backend)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_374():
    assert split_binary_op(
        'sum(rate(traefik_backend_requests_total{code=~"4.*"}[3m])) by (backend) / sum(rate(traefik_backend_requests_total[3m])) by (backend) * 100 > 5'
    ) == {
        "code": '((sum(rate(traefik_backend_requests_total{code=~"4.*"}[3m])) by '
        "(backend) / sum(rate(traefik_backend_requests_total[3m])) by "
        "(backend)) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(traefik_backend_requests_total{code=~"4.*"}[3m])) '
            "by (backend) / "
            "sum(rate(traefik_backend_requests_total[3m])) by "
            "(backend)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_375():
    assert split_binary_op(
        'sum(rate(traefik_backend_requests_total{code=~"5.*"}[3m])) by (backend) / sum(rate(traefik_backend_requests_total[3m])) by (backend) * 100 > 5'
    ) == {
        "code": '((sum(rate(traefik_backend_requests_total{code=~"5.*"}[3m])) by '
        "(backend) / sum(rate(traefik_backend_requests_total[3m])) by "
        "(backend)) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(traefik_backend_requests_total{code=~"5.*"}[3m])) '
            "by (backend) / "
            "sum(rate(traefik_backend_requests_total[3m])) by "
            "(backend)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_376():
    assert split_binary_op(
        "count(traefik_service_server_up) by (service) == 0"
    ) == {
        "code": "count(traefik_service_server_up) by (service) == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "count(traefik_service_server_up) by (service)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_377():
    assert split_binary_op(
        'sum(rate(traefik_service_requests_total{code=~"4.*"}[3m])) by (service) / sum(rate(traefik_service_requests_total[3m])) by (service) * 100 > 5'
    ) == {
        "code": '((sum(rate(traefik_service_requests_total{code=~"4.*"}[3m])) by '
        "(service) / sum(rate(traefik_service_requests_total[3m])) by "
        "(service)) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(traefik_service_requests_total{code=~"4.*"}[3m])) '
            "by (service) / "
            "sum(rate(traefik_service_requests_total[3m])) by "
            "(service)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_378():
    assert split_binary_op(
        'sum(rate(traefik_service_requests_total{code=~"5.*"}[3m])) by (service) / sum(rate(traefik_service_requests_total[3m])) by (service) * 100 > 5'
    ) == {
        "code": '((sum(rate(traefik_service_requests_total{code=~"5.*"}[3m])) by '
        "(service) / sum(rate(traefik_service_requests_total[3m])) by "
        "(service)) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(traefik_service_requests_total{code=~"5.*"}[3m])) '
            "by (service) / "
            "sum(rate(traefik_service_requests_total[3m])) by "
            "(service)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_379():
    assert split_binary_op("haproxy_up == 0") == {
        "code": "haproxy_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "haproxy_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_380():
    assert split_binary_op(
        'sum by (backend) (rate(haproxy_server_http_responses_total{code="4xx"}[1m])) / sum by (backend) (rate(haproxy_server_http_responses_total[1m]) * 100) > 5'
    ) == {
        "code": '(sum(rate(haproxy_server_http_responses_total{code="4xx"}[1m])) '
        "by (backend) / sum(rate(haproxy_server_http_responses_total[1m]) "
        "* 100) by (backend)) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(haproxy_server_http_responses_total{code="4xx"}[1m])) '
            "by (backend) / "
            "sum(rate(haproxy_server_http_responses_total[1m]) * "
            "100) by (backend)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_381():
    assert split_binary_op(
        'sum by (backend) (rate(haproxy_server_http_responses_total{code="5xx"}[1m])) / sum by (backend) (rate(haproxy_server_http_responses_total[1m]) * 100) > 5'
    ) == {
        "code": '(sum(rate(haproxy_server_http_responses_total{code="5xx"}[1m])) '
        "by (backend) / sum(rate(haproxy_server_http_responses_total[1m]) "
        "* 100) by (backend)) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(haproxy_server_http_responses_total{code="5xx"}[1m])) '
            "by (backend) / "
            "sum(rate(haproxy_server_http_responses_total[1m]) * "
            "100) by (backend)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_382():
    assert split_binary_op(
        'sum by (server) (rate(haproxy_server_http_responses_total{code="4xx"}[1m])) / sum by (server) (rate(haproxy_server_http_responses_total[1m]) * 100) > 5'
    ) == {
        "code": '(sum(rate(haproxy_server_http_responses_total{code="4xx"}[1m])) '
        "by (server) / sum(rate(haproxy_server_http_responses_total[1m]) * "
        "100) by (server)) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(haproxy_server_http_responses_total{code="4xx"}[1m])) '
            "by (server) / "
            "sum(rate(haproxy_server_http_responses_total[1m]) * "
            "100) by (server)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_383():
    assert split_binary_op(
        'sum by (server) (rate(haproxy_server_http_responses_total{code="5xx"}[1m])) / sum by (server) (rate(haproxy_server_http_responses_total[1m]) * 100) > 5'
    ) == {
        "code": '(sum(rate(haproxy_server_http_responses_total{code="5xx"}[1m])) '
        "by (server) / sum(rate(haproxy_server_http_responses_total[1m]) * "
        "100) by (server)) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": 'sum(rate(haproxy_server_http_responses_total{code="5xx"}[1m])) '
            "by (server) / "
            "sum(rate(haproxy_server_http_responses_total[1m]) * "
            "100) by (server)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_384():
    assert split_binary_op(
        "sum by (server) (rate(haproxy_server_response_errors_total[1m])) / sum by (server) (rate(haproxy_server_http_responses_total[1m]) * 100) > 5"
    ) == {
        "code": "(sum(rate(haproxy_server_response_errors_total[1m])) by (server) "
        "/ sum(rate(haproxy_server_http_responses_total[1m]) * 100) by "
        "(server)) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_server_response_errors_total[1m])) "
            "by (server) / "
            "sum(rate(haproxy_server_http_responses_total[1m]) * "
            "100) by (server)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_385():
    assert split_binary_op(
        "sum by (backend) (rate(haproxy_backend_connection_errors_total[1m])) > 100"
    ) == {
        "code": "sum(rate(haproxy_backend_connection_errors_total[1m])) by "
        "(backend) > 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_backend_connection_errors_total[1m])) "
            "by (backend)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_386():
    assert split_binary_op(
        "sum by (server) (rate(haproxy_server_connection_errors_total[1m])) > 100"
    ) == {
        "code": "sum(rate(haproxy_server_connection_errors_total[1m])) by (server) "
        "> 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_server_connection_errors_total[1m])) "
            "by (server)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_387():
    assert split_binary_op(
        "((sum by (backend) (avg_over_time(haproxy_backend_max_sessions[2m])) / sum by (backend) (avg_over_time(haproxy_backend_limit_sessions[2m]))) * 100) > 80"
    ) == {
        "code": "((sum(avg_over_time(haproxy_backend_max_sessions[2m])) by "
        "(backend) / "
        "sum(avg_over_time(haproxy_backend_limit_sessions[2m])) by "
        "(backend)) * 100) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(sum(avg_over_time(haproxy_backend_max_sessions[2m])) "
            "by (backend) / "
            "sum(avg_over_time(haproxy_backend_limit_sessions[2m])) "
            "by (backend)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_388():
    assert split_binary_op(
        "sum by (backend) (haproxy_backend_current_queue) > 0"
    ) == {
        "code": "sum(haproxy_backend_current_queue) by (backend) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(haproxy_backend_current_queue) by (backend)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_389():
    assert split_binary_op(
        "avg by (backend) (haproxy_backend_http_total_time_average_seconds) > 1"
    ) == {
        "code": "avg(haproxy_backend_http_total_time_average_seconds) by (backend) "
        "> 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "avg(haproxy_backend_http_total_time_average_seconds) "
            "by (backend)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_390():
    assert split_binary_op(
        "sum by (backend) (rate(haproxy_backend_retry_warnings_total[1m])) > 10"
    ) == {
        "code": "sum(rate(haproxy_backend_retry_warnings_total[1m])) by (backend) "
        "> 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_backend_retry_warnings_total[1m])) "
            "by (backend)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_391():
    assert split_binary_op("haproxy_backend_up == 0") == {
        "code": "haproxy_backend_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "haproxy_backend_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_392():
    assert split_binary_op("haproxy_server_up == 0") == {
        "code": "haproxy_server_up == 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "haproxy_server_up",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_393():
    assert split_binary_op(
        "sum by (frontend) (rate(haproxy_frontend_requests_denied_total[2m])) > 10"
    ) == {
        "code": "sum(rate(haproxy_frontend_requests_denied_total[2m])) by "
        "(frontend) > 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_frontend_requests_denied_total[2m])) "
            "by (frontend)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_394():
    assert split_binary_op(
        "increase(haproxy_server_check_failures_total[1m]) > 0"
    ) == {
        "code": "increase(haproxy_server_check_failures_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(haproxy_server_check_failures_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_395():
    assert split_binary_op(
        '((sum by (proxy) (rate(haproxy_server_http_responses_total{code="4xx"}[1m])) / sum by (proxy) (rate(haproxy_server_http_responses_total[1m]))) * 100) > 5'
    ) == {
        "code": '((sum(rate(haproxy_server_http_responses_total{code="4xx"}[1m])) '
        "by (proxy) / sum(rate(haproxy_server_http_responses_total[1m])) "
        "by (proxy)) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(haproxy_server_http_responses_total{code="4xx"}[1m])) '
            "by (proxy) / "
            "sum(rate(haproxy_server_http_responses_total[1m])) by "
            "(proxy)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_396():
    assert split_binary_op(
        '((sum by (proxy) (rate(haproxy_server_http_responses_total{code="5xx"}[1m])) / sum by (proxy) (rate(haproxy_server_http_responses_total[1m]))) * 100) > 5'
    ) == {
        "code": '((sum(rate(haproxy_server_http_responses_total{code="5xx"}[1m])) '
        "by (proxy) / sum(rate(haproxy_server_http_responses_total[1m])) "
        "by (proxy)) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(haproxy_server_http_responses_total{code="5xx"}[1m])) '
            "by (proxy) / "
            "sum(rate(haproxy_server_http_responses_total[1m])) by "
            "(proxy)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_397():
    assert split_binary_op(
        '((sum by (server) (rate(haproxy_server_http_responses_total{code="4xx"}[1m])) / sum by (server) (rate(haproxy_server_http_responses_total[1m]))) * 100) > 5'
    ) == {
        "code": '((sum(rate(haproxy_server_http_responses_total{code="4xx"}[1m])) '
        "by (server) / sum(rate(haproxy_server_http_responses_total[1m])) "
        "by (server)) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(haproxy_server_http_responses_total{code="4xx"}[1m])) '
            "by (server) / "
            "sum(rate(haproxy_server_http_responses_total[1m])) by "
            "(server)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_398():
    assert split_binary_op(
        '((sum by (server) (rate(haproxy_server_http_responses_total{code="5xx"}[1m])) / sum by (server) (rate(haproxy_server_http_responses_total[1m]))) * 100) > 5'
    ) == {
        "code": '((sum(rate(haproxy_server_http_responses_total{code="5xx"}[1m])) '
        "by (server) / sum(rate(haproxy_server_http_responses_total[1m])) "
        "by (server)) * 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": '(sum(rate(haproxy_server_http_responses_total{code="5xx"}[1m])) '
            "by (server) / "
            "sum(rate(haproxy_server_http_responses_total[1m])) by "
            "(server)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_399():
    assert split_binary_op(
        "(sum by (server) (rate(haproxy_server_response_errors_total[1m])) / sum by (server) (rate(haproxy_server_http_responses_total[1m]))) * 100 > 5"
    ) == {
        "code": "((sum(rate(haproxy_server_response_errors_total[1m])) by (server) "
        "/ sum(rate(haproxy_server_http_responses_total[1m])) by (server)) "
        "* 100) > 5",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(sum(rate(haproxy_server_response_errors_total[1m])) "
            "by (server) / "
            "sum(rate(haproxy_server_http_responses_total[1m])) by "
            "(server)) * 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_400():
    assert split_binary_op(
        "(sum by (proxy) (rate(haproxy_backend_connection_errors_total[1m]))) > 100"
    ) == {
        "code": "sum(rate(haproxy_backend_connection_errors_total[1m])) by (proxy) "
        "> 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_backend_connection_errors_total[1m])) "
            "by (proxy)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_401():
    assert split_binary_op(
        "(sum by (proxy) (rate(haproxy_server_connection_errors_total[1m]))) > 100"
    ) == {
        "code": "sum(rate(haproxy_server_connection_errors_total[1m])) by (proxy) "
        "> 100",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_server_connection_errors_total[1m])) "
            "by (proxy)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_402():
    assert split_binary_op(
        "((haproxy_server_max_sessions >0) * 100) / (haproxy_server_limit_sessions > 0) > 80"
    ) == {
        "code": "(((haproxy_server_max_sessions > 0) * 100) / "
        "(haproxy_server_limit_sessions > 0)) > 80",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "((haproxy_server_max_sessions > 0) * 100) / "
            "(haproxy_server_limit_sessions > 0)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_403():
    assert split_binary_op(
        "sum by (proxy) (rate(haproxy_backend_current_queue[2m])) > 0"
    ) == {
        "code": "sum(rate(haproxy_backend_current_queue[2m])) by (proxy) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_backend_current_queue[2m])) by "
            "(proxy)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_404():
    assert split_binary_op(
        "avg by (instance, proxy) (haproxy_backend_max_total_time_seconds) > 1"
    ) == {
        "code": "avg(haproxy_backend_max_total_time_seconds) by (instance, proxy) "
        "> 1",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "avg(haproxy_backend_max_total_time_seconds) by "
            "(instance, proxy)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "1",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_405():
    assert split_binary_op(
        "sum by (proxy) (rate(haproxy_backend_retry_warnings_total[1m])) > 10"
    ) == {
        "code": "sum(rate(haproxy_backend_retry_warnings_total[1m])) by (proxy) > "
        "10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_backend_retry_warnings_total[1m])) "
            "by (proxy)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_406():
    assert split_binary_op(
        "haproxy_backend_active_servers + haproxy_backend_backup_servers == 0"
    ) == {
        "code": "(haproxy_backend_active_servers + haproxy_backend_backup_servers) "
        "== 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "haproxy_backend_active_servers + "
            "haproxy_backend_backup_servers",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_407():
    assert split_binary_op(
        "sum by (proxy) (rate(haproxy_frontend_denied_connections_total[2m])) > 10"
    ) == {
        "code": "sum(rate(haproxy_frontend_denied_connections_total[2m])) by "
        "(proxy) > 10",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "sum(rate(haproxy_frontend_denied_connections_total[2m])) "
            "by (proxy)",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "10",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_408():
    assert split_binary_op(
        "increase(haproxy_server_check_failures_total[1m]) > 0"
    ) == {
        "code": "increase(haproxy_server_check_failures_total[1m]) > 0",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "increase(haproxy_server_check_failures_total[1m])",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_409():
    assert split_binary_op(
        "vmware_vm_mem_usage_average / 100 >= 80 and vmware_vm_mem_usage_average / 100 < 90"
    ) == {
        "code": "((vmware_vm_mem_usage_average / 100) >= 80) and "
        "((vmware_vm_mem_usage_average / 100) < 90)",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(vmware_vm_mem_usage_average / 100) >= 80",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "vmware_vm_mem_usage_average / 100",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">=",
            "right": {
                "code": "80",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "(vmware_vm_mem_usage_average / 100) < 90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": True,
            "join_modifier": {"args": None, "op": ""},
            "left": {
                "code": "vmware_vm_mem_usage_average / 100",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "<",
            "right": {
                "code": "90",
                "group_modifier": {"args": None, "op": ""},
                "is_binary_op": False,
                "join_modifier": {"args": None, "op": ""},
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_410():
    assert split_binary_op("vmware_vm_mem_usage_average / 100 >= 90") == {
        "code": "(vmware_vm_mem_usage_average / 100) >= 90",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "vmware_vm_mem_usage_average / 100",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">=",
        "right": {
            "code": "90",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_411():
    assert split_binary_op("vmware_vm_snapshots > 3") == {
        "code": "vmware_vm_snapshots > 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "vmware_vm_snapshots",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_412():
    assert split_binary_op(
        "(time() - vmware_vm_snapshot_timestamp_seconds) / (60 * 60 * 24) >= 3"
    ) == {
        "code": "((time() - vmware_vm_snapshot_timestamp_seconds) / 86400) >= 3",
        "group_modifier": {"args": None, "op": ""},
        "is_binary_op": True,
        "join_modifier": {"args": None, "op": ""},
        "left": {
            "code": "(time() - vmware_vm_snapshot_timestamp_seconds) / "
            "86400",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">=",
        "right": {
            "code": "3",
            "group_modifier": {"args": None, "op": ""},
            "is_binary_op": False,
            "join_modifier": {"args": None, "op": ""},
            "left": None,
            "op": "",
            "right": None,
        },
    }
