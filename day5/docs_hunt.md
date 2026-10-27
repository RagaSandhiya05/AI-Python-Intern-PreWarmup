# T21 – Documentation Scavenger Hunt

## 1. Requests: What does the `timeout` parameter do?

**Answer:** The `timeout` parameter specifies how long Requests waits without receiving data from the server before raising a timeout exception. It does not limit the total time required to download the entire response.

**Documentation:** https://requests.readthedocs.io/en/latest/user/quickstart/

**Time taken:** 15 minutes

## 2. Dockerfile: What is the difference between `COPY` and `ADD`?

**Answer:** Both instructions add files to a Docker image. `COPY` copies files from the build context or supported build sources. `ADD` also supports remote URLs and Git repositories and can automatically extract local tar archives. Use `COPY` when simple file copying is sufficient.

**Documentation:** https://docs.docker.com/reference/dockerfile/

**Time taken:** 10 minutes

## 3. Python: What does `dict.get()` return for a missing key?

**Answer:** The `dict.get()` method returns `None` if the specified key is missing and no default value is provided. If a default value is provided, it returns that value instead.

Example:

```python
student = {"name": "Raga"}

print(student.get("age"))       # None
print(student.get("age", 20))   # 20
```

**Documentation:** https://docs.python.org/3/library/stdtypes.html#dict.get

**Time taken:** 15 minutes

## 4. FastAPI: How do you declare a query parameter?

**Answer:** Query parameters are declared as function parameters in a FastAPI endpoint when they are not path parameters. Python type hints specify their types, and default values make them optional.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_items(limit: int = 10):
    return {"limit": limit}
```

Example request: `http://127.0.0.1:8000/items/?limit=5`

Here, `limit` is an integer query parameter with a default value of `10`.

**Documentation:** https://fastapi.tiangolo.com/tutorial/query-params/

**Time taken:** 15 minutes

## 5. Docker Compose: What does `docker compose down -v` do?

**Answer:** The command stops and removes the containers and networks created by Docker Compose and removes the named volumes declared in the Compose file and anonymous volumes attached to the containers. External volumes are not removed.

**Documentation:** https://docs.docker.com/reference/cli/docker/compose/down/

**Time taken:** 12 minutes

## 6. Git: What is the difference between `git fetch` and `git pull`?

**Answer:**
- `git fetch` downloads updates from the remote repository and updates remote-tracking references without integrating those changes into the current branch.
- `git pull` fetches remote updates and then integrates them into the current branch, typically through a fast-forward, merge, or rebase depending on configuration.

**Fetch documentation:** https://git-scm.com/docs/git-fetch

**Pull documentation:** https://git-scm.com/docs/git-pull

**Time taken:** 9 minutes

---

## Reflection

This task helped me understand official documentation and find answers about Python, HTTP requests, Docker, FastAPI, and Git. I practised reading technical references and identifying the relevant information.

**Total time taken:** 76 minutes
