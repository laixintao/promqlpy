from promqlpy import split_binary_op


def test_case_0():
    assert split_binary_op("pg_up == 0") == {
        "code": "pg_up == 0",
        "is_binary_op": True,
        "left": {
            "code": "pg_up",
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "==",
        "right": {
            "code": "0",
            "is_binary_op": False,
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
        "is_binary_op": True,
        "left": {
            "code": "time() - pg_postmaster_start_time_seconds",
            "is_binary_op": True,
            "left": {
                "code": "time()",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "-",
            "right": {
                "code": "pg_postmaster_start_time_seconds",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "<",
        "right": {
            "code": "60",
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_2():
    assert split_binary_op("pg_exporter_last_scrape_error > 0") == {
        "code": "pg_exporter_last_scrape_error > 0",
        "is_binary_op": True,
        "left": {
            "code": "pg_exporter_last_scrape_error",
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "0",
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_3():
    assert split_binary_op(
        "pg_replication_lag > 30 and ON(instance) pg_replication_is_replica"
        " == 1"
    ) == {
        "code": (
            "(pg_replication_lag > 30) and on (instance) "
            "(pg_replication_is_replica == 1)"
        ),
        "is_binary_op": True,
        "left": {
            "code": "pg_replication_lag > 30",
            "is_binary_op": True,
            "left": {
                "code": "pg_replication_lag",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "30",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "pg_replication_is_replica == 1",
            "is_binary_op": True,
            "left": {
                "code": "pg_replication_is_replica",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
            "op": "==",
            "right": {
                "code": "1",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_4():
    assert split_binary_op(
        "(pg_stat_user_tables_last_autovacuum > 0) and (time() -"
        " pg_stat_user_tables_last_autovacuum) > 60 * 60 * 24 * 10"
    ) == {
        "code": (
            "(pg_stat_user_tables_last_autovacuum > 0) and ((time() - "
            "pg_stat_user_tables_last_autovacuum) > 864000)"
        ),
        "is_binary_op": True,
        "left": {
            "code": "pg_stat_user_tables_last_autovacuum > 0",
            "is_binary_op": True,
            "left": {
                "code": "pg_stat_user_tables_last_autovacuum",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "(time() - pg_stat_user_tables_last_autovacuum) > 864000",
            "is_binary_op": True,
            "left": {
                "code": "time() - pg_stat_user_tables_last_autovacuum",
                "is_binary_op": True,
                "left": {
                    "code": "time()",
                    "is_binary_op": False,
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": "-",
                "right": {
                    "code": "pg_stat_user_tables_last_autovacuum",
                    "is_binary_op": False,
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
            "op": ">",
            "right": {
                "code": "864000",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_5():
    assert split_binary_op(
        "(pg_stat_user_tables_last_autoanalyze > 0) and (time() -"
        " pg_stat_user_tables_last_autoanalyze) > 24 * 60 * 60 * 10"
    ) == {
        "code": (
            "(pg_stat_user_tables_last_autoanalyze > 0) and ((time() - "
            "pg_stat_user_tables_last_autoanalyze) > 864000)"
        ),
        "is_binary_op": True,
        "left": {
            "code": "pg_stat_user_tables_last_autoanalyze > 0",
            "is_binary_op": True,
            "left": {
                "code": "pg_stat_user_tables_last_autoanalyze",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
            "op": ">",
            "right": {
                "code": "0",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
        },
        "op": "and",
        "right": {
            "code": "(time() - pg_stat_user_tables_last_autoanalyze) > 864000",
            "is_binary_op": True,
            "left": {
                "code": "time() - pg_stat_user_tables_last_autoanalyze",
                "is_binary_op": True,
                "left": {
                    "code": "time()",
                    "is_binary_op": False,
                    "left": None,
                    "op": "",
                    "right": None,
                },
                "op": "-",
                "right": {
                    "code": "pg_stat_user_tables_last_autoanalyze",
                    "is_binary_op": False,
                    "left": None,
                    "op": "",
                    "right": None,
                },
            },
            "op": ">",
            "right": {
                "code": "864000",
                "is_binary_op": False,
                "left": None,
                "op": "",
                "right": None,
            },
        },
    }


def test_case_7():
    assert split_binary_op(
        "sum by (datname)"
        ' (pg_stat_activity_count{datname!~"template.*|postgres"}) < 5'
    ) == {
        "code": (
            'sum(pg_stat_activity_count{datname!~"template.*|postgres"}) by '
            "(datname) < 5"
        ),
        "is_binary_op": True,
        "left": {
            "code": (
                'sum(pg_stat_activity_count{datname!~"template.*|postgres"}) '
                "by (datname)"
            ),
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
        "op": "<",
        "right": {
            "code": "5",
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
    }


def test_case_8():
    assert split_binary_op(
        'increase(pg_stat_database_deadlocks{datname!~"template.*|postgres"}[1m]) > 5'
    ) == {
        "code": (
            'increase(pg_stat_database_deadlocks{datname!~"template.*|postgres"}[1m]) '
            "> 5"
        ),
        "is_binary_op": True,
        "left": {
            "code": 'increase(pg_stat_database_deadlocks{datname!~"template.*|postgres"}[1m])',
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
        "op": ">",
        "right": {
            "code": "5",
            "is_binary_op": False,
            "left": None,
            "op": "",
            "right": None,
        },
    }

def test_case_6():
    assert split_binary_op('sum by (datname) (pg_stat_activity_count{datname!~"template.*|postgres"}) > pg_settings_max_connections * 0.8') == {   'code': 'sum(pg_stat_activity_count{datname!~"template.*|postgres"}) by '
            '(datname) > (pg_settings_max_connections * 0.8)',
    'is_binary_op': True,
    'left': {   'code': 'sum(pg_stat_activity_count{datname!~"template.*|postgres"}) '
                        'by (datname)',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '>',
    'right': {   'code': 'pg_settings_max_connections * 0.8',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_9():
    assert split_binary_op('rate(pg_stat_database_xact_rollback{datname!~"template.*"}[3m]) / rate(pg_stat_database_xact_commit{datname!~"template.*"}[3m]) > 0.02') == {   'code': '(rate(pg_stat_database_xact_rollback{datname!~"template.*"}[3m]) '
            '/ rate(pg_stat_database_xact_commit{datname!~"template.*"}[3m])) '
            '> 0.02',
    'is_binary_op': True,
    'left': {   'code': 'rate(pg_stat_database_xact_rollback{datname!~"template.*"}[3m]) '
                        '/ '
                        'rate(pg_stat_database_xact_commit{datname!~"template.*"}[3m])',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '>',
    'right': {   'code': '0.02',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_10():
    assert split_binary_op('rate(pg_stat_database_xact_commit[1m]) < 10') == {   'code': 'rate(pg_stat_database_xact_commit[1m]) < 10',
    'is_binary_op': True,
    'left': {   'code': 'rate(pg_stat_database_xact_commit[1m])',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '<',
    'right': {   'code': '10',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_11():
    assert split_binary_op('rate(pg_txid_current[1m]) < 5') == {   'code': 'rate(pg_txid_current[1m]) < 5',
    'is_binary_op': True,
    'left': {   'code': 'rate(pg_txid_current[1m])',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '<',
    'right': {   'code': '5',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_12():
    assert split_binary_op('rate(postgresql_errors_total{type="statement_timeout"}[1m]) > 3') == {   'code': 'rate(postgresql_errors_total{type="statement_timeout"}[1m]) > 3',
    'is_binary_op': True,
    'left': {   'code': 'rate(postgresql_errors_total{type="statement_timeout"}[1m])',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '>',
    'right': {   'code': '3',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_13():
    assert split_binary_op('increase(postgresql_errors_total{type="deadlock_detected"}[1m]) > 1') == {   'code': 'increase(postgresql_errors_total{type="deadlock_detected"}[1m]) > '
            '1',
    'is_binary_op': True,
    'left': {   'code': 'increase(postgresql_errors_total{type="deadlock_detected"}[1m])',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '>',
    'right': {   'code': '1',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_14():
    assert split_binary_op('pg_replication_slots_active == 0') == {   'code': 'pg_replication_slots_active == 0',
    'is_binary_op': True,
    'left': {   'code': 'pg_replication_slots_active',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '==',
    'right': {   'code': '0',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_15():
    assert split_binary_op('((pg_stat_user_tables_n_dead_tup > 10000) / (pg_stat_user_tables_n_live_tup + pg_stat_user_tables_n_dead_tup)) >= 0.1 unless ON(instance) (pg_replication_is_replica == 1)') == {   'code': '(((pg_stat_user_tables_n_dead_tup > 10000) / '
            '(pg_stat_user_tables_n_live_tup + '
            'pg_stat_user_tables_n_dead_tup)) >= 0.1) unless on (instance) '
            '(pg_replication_is_replica == 1)',
    'is_binary_op': True,
    'left': {   'code': '((pg_stat_user_tables_n_dead_tup > 10000) / '
                        '(pg_stat_user_tables_n_live_tup + '
                        'pg_stat_user_tables_n_dead_tup)) >= 0.1',
                'is_binary_op': True,
                'left': {   'code': '(pg_stat_user_tables_n_dead_tup > 10000) '
                                    '/ (pg_stat_user_tables_n_live_tup + '
                                    'pg_stat_user_tables_n_dead_tup)',
                            'is_binary_op': False,
                            'left': None,
                            'op': '',
                            'right': None},
                'op': '>=',
                'right': {   'code': '0.1',
                             'is_binary_op': False,
                             'left': None,
                             'op': '',
                             'right': None}},
    'op': 'unless',
    'right': {   'code': 'pg_replication_is_replica == 1',
                 'is_binary_op': True,
                 'left': {   'code': 'pg_replication_is_replica',
                             'is_binary_op': False,
                             'left': None,
                             'op': '',
                             'right': None},
                 'op': '==',
                 'right': {   'code': '1',
                              'is_binary_op': False,
                              'left': None,
                              'op': '',
                              'right': None}}}


def test_case_16():
    assert split_binary_op('count(pg_replication_is_replica == 0) != 1') == {   'code': 'count(pg_replication_is_replica == 0) != 1',
    'is_binary_op': True,
    'left': {   'code': 'count(pg_replication_is_replica == 0)',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '!=',
    'right': {   'code': '1',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_17():
    assert split_binary_op('pg_replication_is_replica and changes(pg_replication_is_replica[1m]) > 0') == {   'code': 'pg_replication_is_replica and '
            '(changes(pg_replication_is_replica[1m]) > 0)',
    'is_binary_op': True,
    'left': {   'code': 'pg_replication_is_replica',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': 'and',
    'right': {   'code': 'changes(pg_replication_is_replica[1m]) > 0',
                 'is_binary_op': True,
                 'left': {   'code': 'changes(pg_replication_is_replica[1m])',
                             'is_binary_op': False,
                             'left': None,
                             'op': '',
                             'right': None},
                 'op': '>',
                 'right': {   'code': '0',
                              'is_binary_op': False,
                              'left': None,
                              'op': '',
                              'right': None}}}


def test_case_18():
    assert split_binary_op('{__name__=~"pg_settings_.*"} != ON(__name__) {__name__=~"pg_settings_([^t]|t[^r]|tr[^a]|tra[^n]|tran[^s]|trans[^a]|transa[^c]|transac[^t]|transact[^i]|transacti[^o]|transactio[^n]|transaction[^_]|transaction_[^r]|transaction_r[^e]|transaction_re[^a]|transaction_rea[^d]|transaction_read[^_]|transaction_read_[^o]|transaction_read_o[^n]|transaction_read_on[^l]|transaction_read_onl[^y]).*"} OFFSET 5m') == {   'code': '{__name__=~"pg_settings_.*"} != on (__name__) '
            '{__name__=~"pg_settings_([^t]|t[^r]|tr[^a]|tra[^n]|tran[^s]|trans[^a]|transa[^c]|transac[^t]|transact[^i]|transacti[^o]|transactio[^n]|transaction[^_]|transaction_[^r]|transaction_r[^e]|transaction_re[^a]|transaction_rea[^d]|transaction_read[^_]|transaction_read_[^o]|transaction_read_o[^n]|transaction_read_on[^l]|transaction_read_onl[^y]).*"} '
            'offset 5m',
    'is_binary_op': True,
    'left': {   'code': '{__name__=~"pg_settings_.*"}',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '!=',
    'right': {   'code': '{__name__=~"pg_settings_([^t]|t[^r]|tr[^a]|tra[^n]|tran[^s]|trans[^a]|transa[^c]|transac[^t]|transact[^i]|transacti[^o]|transactio[^n]|transaction[^_]|transaction_[^r]|transaction_r[^e]|transaction_re[^a]|transaction_rea[^d]|transaction_read[^_]|transaction_read_[^o]|transaction_read_o[^n]|transaction_read_on[^l]|transaction_read_onl[^y]).*"} '
                         'offset 5m',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_19():
    assert split_binary_op('sum(pg_stat_ssl_compression) > 0') == {   'code': 'sum(pg_stat_ssl_compression) > 0',
    'is_binary_op': True,
    'left': {   'code': 'sum(pg_stat_ssl_compression)',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '>',
    'right': {   'code': '0',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_20():
    assert split_binary_op('((sum (pg_locks_count)) / (pg_settings_max_locks_per_transaction * pg_settings_max_connections)) > 0.20') == {   'code': '(sum(pg_locks_count) / (pg_settings_max_locks_per_transaction * '
            'pg_settings_max_connections)) > 0.2',
    'is_binary_op': True,
    'left': {   'code': 'sum(pg_locks_count) / '
                        '(pg_settings_max_locks_per_transaction * '
                        'pg_settings_max_connections)',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '>',
    'right': {   'code': '0.2',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_21():
    assert split_binary_op('pg_bloat_btree_bloat_pct > 80 and on (idxname) (pg_bloat_btree_real_size > 100000000)') == {   'code': '(pg_bloat_btree_bloat_pct > 80) and on (idxname) '
            '(pg_bloat_btree_real_size > 1e+08)',
    'is_binary_op': True,
    'left': {   'code': 'pg_bloat_btree_bloat_pct > 80',
                'is_binary_op': True,
                'left': {   'code': 'pg_bloat_btree_bloat_pct',
                            'is_binary_op': False,
                            'left': None,
                            'op': '',
                            'right': None},
                'op': '>',
                'right': {   'code': '80',
                             'is_binary_op': False,
                             'left': None,
                             'op': '',
                             'right': None}},
    'op': 'and',
    'right': {   'code': 'pg_bloat_btree_real_size > 1e+08',
                 'is_binary_op': True,
                 'left': {   'code': 'pg_bloat_btree_real_size',
                             'is_binary_op': False,
                             'left': None,
                             'op': '',
                             'right': None},
                 'op': '>',
                 'right': {   'code': '1e+08',
                              'is_binary_op': False,
                              'left': None,
                              'op': '',
                              'right': None}}}


def test_case_22():
    assert split_binary_op('pg_bloat_table_bloat_pct > 80 and on (relname) (pg_bloat_table_real_size > 200000000)') == {   'code': '(pg_bloat_table_bloat_pct > 80) and on (relname) '
            '(pg_bloat_table_real_size > 2e+08)',
    'is_binary_op': True,
    'left': {   'code': 'pg_bloat_table_bloat_pct > 80',
                'is_binary_op': True,
                'left': {   'code': 'pg_bloat_table_bloat_pct',
                            'is_binary_op': False,
                            'left': None,
                            'op': '',
                            'right': None},
                'op': '>',
                'right': {   'code': '80',
                             'is_binary_op': False,
                             'left': None,
                             'op': '',
                             'right': None}},
    'op': 'and',
    'right': {   'code': 'pg_bloat_table_real_size > 2e+08',
                 'is_binary_op': True,
                 'left': {   'code': 'pg_bloat_table_real_size',
                             'is_binary_op': False,
                             'left': None,
                             'op': '',
                             'right': None},
                 'op': '>',
                 'right': {   'code': '2e+08',
                              'is_binary_op': False,
                              'left': None,
                              'op': '',
                              'right': None}}}


def test_case_23():
    assert split_binary_op('changes(process_start_time_seconds{job=~"loki"}[15m]) > 2') == {   'code': 'changes(process_start_time_seconds{job=~"loki"}[15m]) > 2',
    'is_binary_op': True,
    'left': {   'code': 'changes(process_start_time_seconds{job=~"loki"}[15m])',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '>',
    'right': {   'code': '2',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_24():
    assert split_binary_op('100 * sum(rate(loki_request_duration_seconds_count{status_code=~"5.."}[1m])) by (namespace, job, route) / sum(rate(loki_request_duration_seconds_count[1m])) by (namespace, job, route) > 10') == {   'code': '((100 * '
            'sum(rate(loki_request_duration_seconds_count{status_code=~"5.."}[1m])) '
            'by (namespace, job, route)) / '
            'sum(rate(loki_request_duration_seconds_count[1m])) by (namespace, '
            'job, route)) > 10',
    'is_binary_op': True,
    'left': {   'code': '(100 * '
                        'sum(rate(loki_request_duration_seconds_count{status_code=~"5.."}[1m])) '
                        'by (namespace, job, route)) / '
                        'sum(rate(loki_request_duration_seconds_count[1m])) by '
                        '(namespace, job, route)',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '>',
    'right': {   'code': '10',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}


def test_case_25():
    assert split_binary_op('sum(increase(loki_panic_total[10m])) by (namespace, job) > 0') == {   'code': 'sum(increase(loki_panic_total[10m])) by (namespace, job) > 0',
    'is_binary_op': True,
    'left': {   'code': 'sum(increase(loki_panic_total[10m])) by (namespace, '
                        'job)',
                'is_binary_op': False,
                'left': None,
                'op': '',
                'right': None},
    'op': '>',
    'right': {   'code': '0',
                 'is_binary_op': False,
                 'left': None,
                 'op': '',
                 'right': None}}

