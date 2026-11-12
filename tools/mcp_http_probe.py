"""Small maintainer JSON-RPC client for a locally forwarded Unreal MCP server."""
import json
import urllib.request


class Client:
    def __init__(self, url):
        self.url=url
        self.session=None
        self.seq=0

    def rpc(self, method, params=None):
        self.seq+=1
        body=json.dumps(dict(jsonrpc='2.0',id=self.seq,method=method,params=params or {})).encode()
        headers={'Content-Type':'application/json','Accept':'application/json, text/event-stream'}
        if self.session:headers['Mcp-Session-Id']=self.session
        req=urllib.request.Request(self.url,body,headers)
        with urllib.request.urlopen(req,timeout=180) as response:
            self.session=response.headers.get('Mcp-Session-Id',self.session)
            raw=response.read().decode()
        if raw.lstrip().startswith('data:') or '\ndata:' in raw:
            raw=next(line[5:].strip() for line in raw.splitlines() if line.startswith('data:'))
        r=json.loads(raw)
        if 'error' in r:raise RuntimeError(json.dumps(r['error']))
        return r.get('result',r)

    def initialize(self):
        return self.rpc('initialize',dict(protocolVersion='2025-03-26',capabilities={},clientInfo={'name':'ACP classroom rehearsal','version':'1'}))

    def call(self,name,arguments=None):
        r=self.rpc('tools/call',dict(name=name,arguments=arguments or {}))
        if r.get('isError'):raise RuntimeError(json.dumps(r))
        return r
