Plugin for CudaText.
Adds items "uroboroSQL Format - ..." to plugins menu to format SQL text.
Lexer name can be any, "SQL" not fixed in install.inf.
Ported from Sublime Text plugin.

Uses uroboroSQL Python lib:
  https://github.com/future-architect

UroboroSQL is often used in enterprise systems, for formatting to a highly maintainable style even for very long SQL.
In particular, in countries where English is not their mother tongue, such as Japan, comments may be included in SELECT clauses. In that case, we will align the vertical position of the AS clause and the comment, pursuing the viewability which can be said as artistic anymore, This was developed to realize this automatically.

--- In case of general formatter
SELECT MI.MAKER_CD AS ITEM_MAKER_CD -- メーカーコード
,
       MI.BRAND_CD AS ITEM_BRAND_CD -- ブランドコード
,
       MI.ITEM_CD AS ITEM_CD -- 商品コード
,
       MI.CATEGORY AS ITEM_CATEGORY -- 商品カテゴリ
FROM M_ITEM MI -- 商品マスタ

WHERE 1 = 1
  AND MI.ARRIVAL_DATE = '2016-12-01' -- 入荷日


--- In case of uroboroSQL formatter
SELECT
    MI.MAKER_CD AS  ITEM_MAKER_CD   -- メーカーコード
,   MI.BRAND_CD AS  ITEM_BRAND_CD   -- ブランドコード
,   MI.ITEM_CD  AS  ITEM_CD         -- 商品コード
,   MI.CATEGORY AS  ITEM_CATEGORY   -- 商品カテゴリ
FROM
    M_ITEM  MI  -- 商品マスタ
WHERE
    1               =   1
AND MI.ARRIVAL_DATE =   '2016-12-01'    -- 入荷日


Options in json file:
- uf_tab_size
  Specify the tab size of the indent after formatting. We recommend 4.
-uf_translate_tabs_to_spaces
  Specify whether the indent after formatting is tab or space. It becomes a space by setting it to true.
- uf_uppercase
  If you want to convert a reserved word and identifier to uppercase specifies true.
- uf_comment_syntax
  It specifies the comment syntax format.
  You can specify the "uroboroSQL" or "doma2".
  In the case of normal SQL, you can specify either.
- uf_escapesequence_u005c
  If you have specified the escape sequence with a backslash in the SQL to specify the true.


Author: Alexey (CudaText)
License: MIT
