import random
import string

def generate_key():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def kill_or_not():
    return random.choice([True,False])

def check(obj):
    if obj.army_count<=0:
        exit(f"{obj.name} has ran out of soldiers or was given a non-positive army count")


class General:
    def __init__(self,name,army_count):
        self.name=name
        self.army_count = army_count
        self.received_messages = 0
        self.sent_messages = 0
        self.confirmed = False
        self.dump = {}
        self.message_sent= ""
        self.recvd_unique_msg_id = ""
        self.message_revcd= ""
        self.check = check

    def army_check(self):
        self.check(self)

    def create_messengers(self,number,message):
        self.message_sent = message
        unique_key = generate_key()
        messengers = []
        for i in range(number):
            messengers.append((i+1,unique_key,message))
            self.sent_messages+=1
            self.army_count -= 1
        return messengers

    def army_count(self):
        return self.army_count

    def receive(self,m):
        if m != "dead":
            self.army_count+=1
            self.received_messages+=1
            if not m[1] in self.dump.keys():
                new = {m[1]:m[2]}
                self.dump.update(new)
                self.recvd_unique_msg_id = m[1]
                self.message_revcd = m[2]
            else:
                self.confirmed=True

class Castle:
    def __init__(self):
        self.kills = 0

    def kill(self,m):
        if kill_or_not():
            self.kills +=1
            return "dead"
        else:
            return m

def passing_through_castle(messengers,castle,general):
    for m in messengers:
        _m = castle.kill(m)
        general.receive(_m)

def summary(castle,general1,general2):
    text = ""
    text+= f"{general1.name} sent {general1.sent_messages} messengers with the message '{general1.message_sent}'.\n" \
        f"Out of which {general1.sent_messages - general2.received_messages} messengers were killed by the castle." \
        f"\nHence, {general2.name} received {general2.received_messages} messages all having same unique id which was '{general2.recvd_unique_msg_id}' and\n" \
        f"he confirmed the receiveing the message by sending {general2.sent_messages} messengers with the message '{general2.message_sent}'.\n" \
        f"Out of which {general2.sent_messages - general1.received_messages} messengers were killed by the castle." \
        f"\nHence, {general1.name} received {general1.received_messages} messages all having same unique id which was '{general1.recvd_unique_msg_id}'."
    stats = f"\n\nArmy Counts:\n\t{general1.name} : {general1.army_count}\n\t{general2.name} : {general2.army_count}\n\nMessengers killed by castle:\n\t{castle.kills}"
    text+=stats
    return text