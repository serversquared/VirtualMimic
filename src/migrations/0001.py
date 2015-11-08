from yoyo import step

step("ALTER TABLE nodes ADD is_input TINYINT")
step("ALTER TABLE nodes ADD is_response TINYINT")
step("ALTER TABLE nodes ADD level int")
