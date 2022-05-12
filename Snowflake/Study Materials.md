- **Creating a table from the other table data:**
 
 CREATE OR REPLACE TABLE NATION 
 AS 
 (SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF100"."NATION")
 
- **Getting the DDL Data**

SELECT GET_DDL('TABLE','NATION')

- **Getting the Columns from the table**

SELECT COLUMN_NAME FROM CITIBIKE.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'NATION'

- **Creating a Stored Procedure using Java language**

Reference link:https://interworks.com/blog/2020/02/18/zero-to-snowflake-simple-sql-stored-procedures/

~~~~sql
create or replace procedure NATION_PROCEDURE()
returns STRING
language javascript
as     
$$  
var sql_command= `INSERT OVERWRITE INTO "CITICAR"."PUBLIC"."NATION" 
("N_NATIONKEY","N_NAME","N_REGIONKEY","N_COMMENT")
SELECT
N_NATIONKEY,N_NAME,N_REGIONKEY,N_COMMENT
FROM "CITIBIKE"."PUBLIC"."NATION";`
var snapshot_statement = snowflake.createStatement({sqlText:sql_command});
var snapshot_results = snapshot_statement.execute();
return true;
$$;
~~~~




 
 
