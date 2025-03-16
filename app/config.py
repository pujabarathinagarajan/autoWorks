# Symplicity API Configuration

# ✅ API URL (Updated with correct endpoint)
SYMPLICITY_JOB_SEARCH_URL = "https://northeastern-csm.symplicity.com/api/v2/jobs"

# ✅ Headers for API request
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Authorization": "Basic 389a31571f68ca0e41f75e03d30b3e30",
    "Sec-Fetch-Site": "same-origin",
    "Accept-Language": "en-IN,en-GB;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Mode": "cors",
    "Host": "northeastern-csm.symplicity.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Referer": "https://northeastern-csm.symplicity.com/students/app/jobs/search?ocr=f&postdate=1&exclude_applied_jobs=1&perPage=20&page=2&sort=!postdate",
    "Connection": "keep-alive",
    "Cookie": (
        "AWSALB=26fGGW3Jyo/fJdPDx7SooUccIJAtEKsWmgioD6kqNiA/BP5GW8ZzG0Hxfgjlk1/aN48xQXlCAb8vuiffXfxgktPlzNWYs8aCLXOFpM7O7phkeMPtUbpLfvRrZkNo; "
        "AWSALBCORS=26fGGW3Jyo/fJdPDx7SooUccIJAtEKsWmgioD6kqNiA/BP5GW8ZzG0Hxfgjlk1/aN48xQXlCAb8vuiffXfxgktPlzNWYs8aCLXOFpM7O7phkeMPtUbpLfvRrZkNo; "
        "_ga_1LV3N39QV7=GS1.1.1742062057.21.1.1742063296.0.0.0; _ga_5F0Z7XNL1G=GS1.1.1742062097.25.1.1742063296.0.0.0; "
        "__utma=110326938.984366400.1740781098.1742025566.1742062098.18; __utmb=110326938.10.9.1742063295655; __utmc=110326938; "
        "__utmz=110326938.1742062098.18.7.utmcsr=neuidmsso.neu.edu|utmccn=(referral)|utmcmd=referral|utmcct=/; "
        "_ga=GA1.1.984366400.1740781098; sympcsm_cookie_check=1; __utmt=1; _ga_5F0Z7XNL1G=deleted; "
        "PHPSESSID=b7e9b52c637e4c2744b31c73d706b299; "
        "5dbade39af3c3a9d9bbd2e9878649ee09c5082959d7ca110b04cb7efdd26c7d4=def5020052314b03b2bc45fb3700575016d300cc160514ba56a0b3a5a92edf96bf4a7b8712e69a26a1c892d1be4dd160867f3606414dc566287323e1b15fea5b84a28e7dfa813a407d8bb62b525122d7843ec51335ec578a38229da5f8"
    ),
    "Sec-Fetch-Dest": "empty",
    "x-requested-system-user": "students"
}

# ✅ Query parameters for fetching jobs
PARAMS = {
    "ocr": "f",
    "postdate": 45,
    "exclude_applied_jobs": 1,
    "perPage": 1000,
    "page": 1,
    "sort": "!postdate",
    "json_mode": "read_only",
    "enable_translation": "false",
    "el_work_term": "62e86769398ef06e8102c40d39502733,37226e910d4151f066cd60e5177508b6"
}
