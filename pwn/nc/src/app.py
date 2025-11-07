import socketserver

with open("/flag", "r") as f:
    FLAG = f.read()


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.send(
            "恭喜你成功使用了nc连接，现在请你回答下面的问题吧!\n\n".encode()
        )

        try:
            # 问题1
            self.request.send("1）你愿意加入网安协会吗?(Y/n) ".encode())
            answer1 = self.request.recv(1024).decode().strip()

            if answer1.upper() != "Y":
                self.request.send("我不喜欢你!\n".encode())
                return

            # 问题2
            self.request.send(
                "2）下面的几种形象中，25届会长会最最最喜欢?\n\n\t\t1.金发御姐\t\t2.金发碧眼幼女\t3.黑长直学姐\t4.双马尾妹妹\n\t\t5.低侧马尾白毛少女\t6.元气辣妹\t7.柔软幼女\t8.金箔巧克力\n请输入选项：".encode()
            )
            answer2 = self.request.recv(1024).decode().strip()

            if answer2 != "5":
                self.request.send("我不喜欢你!\n".encode())
                return

            self.request.send(f"\n我喜欢你！\n\n {FLAG}\n".encode())

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), Handler)
    print(f"Server running on {HOST}:{PORT}")
    server.serve_forever()
