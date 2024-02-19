$.getJSON("data.json")
  .done(function(responseJSON) {
    var App = React.createClass({
      getInitialState: function() {
        return { data: responseJSON };
      },

      reset: function() { this.setState({ data: responseJSON }); },
      filter: function(fn) { this.setState({ data: this.state.data.filter(fn) }); },
      reverse: function() { this.setState({ data: this.state.data.slice().reverse() }); },
      random: function() { this.setState({ data: this.state.data.sort(function() { return Math.random() - 0.5; }) }); },
      map: function() {
        this.setState({
          data: this.state.data.map(function(row) {
            return {
              ...row,
              name: row.name.toLowerCase(),
              age: row.age + 1,
            };
          })
        });
      },

      render: function() {
        var data = this.state.data;
        var headers = data.length > 0 ? Object.keys(data[0]) : [];

        return (
          <div className="App">
            <h1>React App</h1>

            <div className="buttons">
              <button onClick={this.reset} className="reset">
                Reset
              </button>

              <button onClick={() => this.filter((row) => row.id < 90)} className="filter-id">
                Filter ID
              </button>

              <button onClick={() => this.filter((row) => row.name.toLowerCase().includes('k'))} className="filter-name">
                Filter Name
              </button>

              <button onClick={() => this.filter((row) => row.age > 20)} className="filter-age">
                Filter Age
              </button>

              <button onClick={() => this.filter((row) => row.hobbies.includes('swimming'))} className="filter-hobbies">
                Filter Hobbies
              </button>

              <button onClick={this.reverse} className="reverse">
                Reverse
              </button>

              <button onClick={this.random} className="random">
                Random
              </button>

              <button onClick={this.map} className="map">
                Map
              </button>
            </div>

            <h4>Table ({data.length} rows)</h4>

            <table>
              <thead>
                <tr>
                  {headers.map(function(header, index) {
                    return <th key={index}>{header}</th>;
                  })}
                </tr>
              </thead>

              <tbody>
                {data.map(function(row, index) {
                  return (
                    <tr key={index}>
                      {headers.map(function(header, index) {
                        return <td key={index}>{row[header]}</td>;
                      })}
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        );
      }
    });

  ReactDOM.render(
    <App />,
    document.getElementById('app')
  );
});