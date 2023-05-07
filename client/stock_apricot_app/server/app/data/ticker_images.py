_dict = {
        "TSLA": "https://images.unsplash.com/photo-1589382010569-adf44df9a0d6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHRlc2xhJTIwbG9nb3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "AAPL": "https://images.unsplash.com/photo-1585184394271-4c0a47dc59c9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YXBwbGUlMjBsb2dvfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
        "AMZN": "https://images.unsplash.com/photo-1602359337719-a8bcbd1f7b51?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YW1hem9uJTIwbG9nb3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "MSFT": "https://images.unsplash.com/photo-1640763502425-7668dc1e4023?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8bWljcm9zb2Z0fGVufDB8fDB8fA%3D%3D&w=1000&q=80",
        "META": "https://images.unsplash.com/photo-1640441281085-9e2000f3d693?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bWV0YSUyMGxvZ298ZW58MHx8MHx8&auto=format&fit=crop&w=600&q=60",
        "GOOGL": "https://images.unsplash.com/photo-1646627927952-c022e715bafb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjd8fGdvb2dsZSUyMGxvZ298ZW58MHx8MHx8&auto=format&fit=crop&w=600&q=60",
        "NVDA": "https://images.unsplash.com/photo-1662947683280-3be5bfc47075?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bnZpZGlhJTIwbG9nb3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "NIO": "https://images.unsplash.com/photo-1677321302481-bb8ac0feca58?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bmlvJTIwbG9nb3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "AMD": "https://images.unsplash.com/photo-1606963060045-1e3eaa0e6eac?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YW1kJTIwbG9nb3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "GOOG": "https://images.unsplash.com/photo-1511296265581-c2450046447d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8Z29vZ2xlJTIwbG9nb3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "MA": "https://images.unsplash.com/photo-1628625194933-ac2b3c0109e7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bWFzdGVyY2FyZHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "BABA": "https://images.unsplash.com/photo-1598956500798-7b64cf4267f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8YWxpYmFiYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "PFE": "https://images.unsplash.com/photo-1623867822001-7fb160bb22a8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGZpemVyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
        "KO": "https://images.unsplash.com/photo-1589423045402-6074a1bdf723?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y29jYSUyMGNvbGF8ZW58MHx8MHx8&auto=format&fit=crop&w=600&q=60",
        "SHOP": "https://images.unsplash.com/photo-1586898633445-fc34716255b2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8c2hvcGlmeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "PEP": "https://images.unsplash.com/photo-1651763174896-27376999056e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8cGVwc2ljb3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60",
        "TM": "https://images.unsplash.com/photo-1647031360882-18f3291420b3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8dG95b3RhJTIwbW90b3JzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
        "AZ": "https://media.istockphoto.com/id/1273007576/photo/green-board-writing-with-white-chalk-stick-a2z.jpg?b=1&s=170667a&w=0&k=20&c=aRsOM2f60ZYb9My99Zj9IdQuRhk_t0W2ygnrNlrkJSs=",
        "ORCL": "https://images.unsplash.com/photo-1662947774718-fd9ae8ca9974?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8b3JhY2xlJTIwbG9nb3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60"

}


def get_ticker_images() -> dict:
    return _dict
