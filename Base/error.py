class Error:
    WRONG_USERNAME = 1020
    EXIST_NICKNAME = 1019
    LOGIN_AGAIN = 1018
    FROZEN_USER = 1017
    NOT_YOUR_WORK = 1016
    NOT_UNDER_REVIEW = 1015
    WORK_IS_PRIVATE = 1014
    WORK_HAS_DELETED = 1013
    NOT_FOUND_WORK_ID = 1012
    NOT_FOUND_WORK_TYPE = 1011
    NOT_FOUND_FILE = 1010
    NEED_REVIEWER = 1009
    NEED_WRITER = 1008
    NO_PASSWORD_LOGIN = 1007
    DENY_LOGIN = 1006
    NEED_LOGIN = 1005
    WRONG_PASSWORD = 1004
    NOT_FOUND_USERNAME = 1003
    NEED_PARAM = 1002
    NEED_JSON = 1001
    NOT_FOUND_ERROR = 1000
    UNKNOWN = 1

    ERROR_DICT = [
        (UNKNOWN, "未知错误"),
        (NOT_FOUND_ERROR, "不存在的错误"),
        (NEED_JSON, "需要JSON数据"),
        (NEED_PARAM, "参数不完整"),
        (NOT_FOUND_USERNAME, "不存在的用户名"),
        (WRONG_PASSWORD, "用户名或密码错误"),
        (NEED_LOGIN, "尚未登录"),
        (DENY_LOGIN, "已经登录"),
        (NO_PASSWORD_LOGIN, "已开启免密登录"),
        (NEED_WRITER, "需要作者登录"),
        (NEED_REVIEWER, "需要审稿员登录"),
        (NOT_FOUND_FILE, "没有上传的文件"),
        (NOT_FOUND_WORK_TYPE, "不存在的作品类型"),
        (NOT_FOUND_WORK_ID, "不存在的作品"),
        (WORK_HAS_DELETED, "作品已被删除"),
        (WORK_IS_PRIVATE, "作品没有公开"),
        (NOT_UNDER_REVIEW, "作品不在审阅状态"),
        (NOT_YOUR_WORK, "不是你上传的作品"),
        (FROZEN_USER, "账号被冻结，请联系社长"),
        (LOGIN_AGAIN, "重新登录"),
        (EXIST_NICKNAME, "已存在的昵称"),
        (WRONG_USERNAME, "错误的账号"),
    ]