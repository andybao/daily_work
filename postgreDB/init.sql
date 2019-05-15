CREATE TABLE data_flows (
    data_flow VARCHAR(50) PRIMARY KEY
);

CREATE TABLE testing_types (
    testing_type VARCHAR(50) PRIMARY KEY
);

CREATE TABLE testing_states (
    testing_state VARCHAR(20) PRIMARY KEY
);

CREATE TABLE testers (
    -- chainvu employee mail address only
    tester VARCHAR (20) PRIMARY KEY CHECK(tester LIKE '%@chainvu.com')
);

CREATE TABLE envs (
    env_uuid VARCHAR(50) PRIMARY KEY,
    zone_hw VARCHAR(50) UNIQUE,
    zone_sw VARCHAR(50),
    site_hw VARCHAR(50) UNIQUE,
    site_sw VARCHAR(50),
    sensor_hw VARCHAR(50) UNIQUE,
    sensor_sw VARCHAR(50),
    cloud_hw VARCHAR(50),
    cloud_sw VARCHAR(50)
);

CREATE TABLE cases (
    case_uuid VARCHAR(50) PRIMARY KEY,
    -- Use data_flow and testing_type to find python script
    data_flow VARCHAR(50) NOT NULL REFERENCES data_flows,
    testing_type VARCHAR(50) NOT NULL REFERENCES testing_types,
    title TEXT NOT NULL UNIQUE,
    expect_result TEXT NOT NULL
);

CREATE TABLE testings (
    testing_uuid VARCHAR(50) PRIMARY KEY,
    env_uuid VARCHAR(50) NOT NULL REFERENCES envs,
    -- Use data_flow and testing_type to filter testings on frontend
    data_flow VARCHAR(50) NOT NULL REFERENCES data_flows,
    testing_type VARCHAR(50) NOT NULL REFERENCES testing_types,
    tester VARCHAR(20) NOT NULL REFERENCES testers,
    running_time TIMESTAMP DEFAULT NOW()
);

CREATE TABLE results (
    result_uuid VARCHAR(50) PRIMARY KEY,
    case_uuid VARCHAR(50) NOT NULL REFERENCES cases,
    testing_state VARCHAR(20) NOT NULL REFERENCES testing_states,
    testing_uuid VARCHAR(50) NOT NULL REFERENCES testings,
    result_json JSON,
    testing_log TEXT,
    comments TEXT,
    running_time TIMESTAMP DEFAULT NOW()
);

INSERT INTO data_flows VALUES ('custom');
INSERT INTO data_flows VALUES ('cloud');
INSERT INTO data_flows VALUES ('zone_manager');
INSERT INTO data_flows VALUES ('zone_manager_and_cloud');

INSERT INTO testing_types VALUES ('custom');
INSERT INTO testing_types VALUES ('sanity');
INSERT INTO testing_types VALUES ('scalability');

INSERT INTO testing_states VALUES ('Passed');
INSERT INTO testing_states VALUES ('Failed');
INSERT INTO testing_states VALUES ('No Run');
INSERT INTO testing_states VALUES ('On Going');
INSERT INTO testing_states VALUES ('Not Applicable');

INSERT INTO testers VALUES ('abao@chainvu.com')